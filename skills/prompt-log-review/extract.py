#!/usr/bin/env python3
"""prompt-log-review 추출기 — 세션 JSONL에서 사용자 프롬프트만 결정론적으로 뽑는다.

사용:
  extract.py --list          최근 세션 나열 (여기서 지목)
  extract.py <JSONL 경로>    user 프롬프트를 [번호] 목록으로 출력
  --since YYYY-MM-DD         그 날짜(로컬 0시) 이후에 쓴 프롬프트만 — 주간 채점이 지난주 것을 다시 세지 않게
필터는 전부 코드다 — LLM 판단 없음. 토큰 0.
"""
import argparse, glob, json, os, re, sys, time
from datetime import datetime

SKIP_MARKERS = ("<command-name>", "<local-command-stdout>", "<task-notification>",
                "<bash-input>", "<bash-stdout>")
# 봉투 없이 본문만 남는 맨몸 슬래시 커맨드("/compact"). 인자가 붙으면(공백 포함) 진짜 요청이라 살린다.
# 경로("/Users/…")는 두 번째 슬래시 때문에 매치되지 않는다.
BARE_SLASH_CMD = re.compile(r"^/[A-Za-z][\w-]*$")
SKIP_PREFIXES = (
    "[Request interrupted by user",
    "This session is being continued from a previous conversation",
    # Orca/멀티세션 오케스트레이션 주입 — 사람 프롬프트 아님 (첫 주간 자동 채점에서 발견)
    "--- Orchestration Messages",
    "Another Claude session sent a message:",
)
MIN_LEN = 5       # 미만 = 맞장구("그래용" 3자, "ㅇㅇ 해" 4자) → 제외. 6자부터는 "다시 진행해" 같은 진짜 명령이라 살린다
TRUNC = 500       # 초과분 절단
WARN_COUNT = 40   # 초과 시 경고 → 스킬이 범위를 물어야 함


def _ts(o):
    try:
        return datetime.fromisoformat(o["timestamp"]).timestamp()
    except (KeyError, TypeError, ValueError):
        return None


def user_texts(path, since=None):
    """since(epoch)가 주어지면 그 이후 프롬프트만. timestamp 없는 레코드는 제외(재채점보다 누락이 낫다)."""
    out = []
    for line in open(path, encoding="utf-8"):
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(o, dict):
            continue
        if o.get("type") != "user" or o.get("isSidechain") or o.get("isMeta"):
            continue
        if since is not None and (_ts(o) or 0) < since:
            continue
        c = o.get("message", {}).get("content")
        if isinstance(c, str):
            txt = c
        elif isinstance(c, list):
            txt = "\n".join(b.get("text", "") for b in c
                            if isinstance(b, dict) and b.get("type") == "text")
        else:
            continue
        txt = txt.strip()
        if not txt or len(txt) < MIN_LEN:
            continue
        if txt.startswith(SKIP_PREFIXES):
            continue
        if txt.startswith("<") and any(m in txt for m in SKIP_MARKERS):
            continue
        if BARE_SLASH_CMD.match(txt):
            continue
        out.append(txt)
    # 연속 재전송 dedup: 직전 항목이 현재 항목의 접두면 직전 것을 버린다
    deduped = []
    for t in out:
        if deduped and t.startswith(deduped[-1]):
            deduped.pop()
        deduped.append(t)
    return deduped


def pick_best(files, cutoff):
    """cutoff 이후에 쓴 사람 프롬프트가 최다인 세션 1개 — 주간 자동 실행의 채점 대상 선정.
    세션 누적 개수가 아니라 창 안의 개수로 센다(오래 열어둔 세션이 매주 뽑혀 같은 프롬프트를 재채점하던 버그).
    워커 세션(orca-workspaces)은 경로로 선제 제외한다(내용 기반 판정은 스킬 몫)."""
    best, best_n = None, 0
    for f in files:
        if "orca-workspaces" in f or os.path.getmtime(f) < cutoff:
            continue
        n = len(user_texts(f, cutoff))
        if n > best_n:
            best, best_n = f, n
    return best, best_n


def cmd_pick(since):
    files = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
    best, n = pick_best(files, since)
    if best:
        print(best)                                  # stdout = 경로만 (스크립트가 그대로 넘긴다)
        print(f"프롬프트 {n}개", file=sys.stderr)


def cmd_list(n=15):
    files = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
    files.sort(key=os.path.getmtime, reverse=True)
    for f in files[:n]:
        proj = os.path.basename(os.path.dirname(f))
        mt = time.strftime("%m-%d %H:%M", time.localtime(os.path.getmtime(f)))
        print(f"{mt} | {os.path.getsize(f)//1024:>6}KB | {proj} | {f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("session", nargs="?", help="세션 JSONL 경로")
    ap.add_argument("--list", action="store_true", help="최근 세션 나열")
    ap.add_argument("--pick", action="store_true",
                    help="--since 이후(기본 7일 전) 사람 프롬프트 최다 세션 경로 1개 출력 (주간 자동 실행용)")
    ap.add_argument("--since", help="YYYY-MM-DD — 이 날짜 로컬 0시 이후 프롬프트만")
    a = ap.parse_args()
    since = time.mktime(time.strptime(a.since, "%Y-%m-%d")) if a.since else None
    if a.pick:
        cmd_pick(since if since is not None else time.time() - 7 * 86400)
        return
    if a.list or not a.session:
        cmd_list()
        return
    prompts = user_texts(a.session, since)
    if len(prompts) > WARN_COUNT:
        print(f"⚠️ 프롬프트 {len(prompts)}개 — 채점 전에 범위를 좁혀라 (예: 최근 N개)\n")
    for i, t in enumerate(prompts, 1):
        if len(t) > TRUNC:
            t = t[:TRUNC] + " …[절단됨]"
        print(f"[{i}] " + t.replace("\n", " ⏎ "))
        print()


if __name__ == "__main__":
    main()
