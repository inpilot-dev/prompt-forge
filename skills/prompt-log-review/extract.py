#!/usr/bin/env python3
"""prompt-log-review 추출기 — 세션 JSONL에서 사용자 프롬프트만 결정론적으로 뽑는다.

사용:
  extract.py --list          최근 세션 나열 (여기서 지목)
  extract.py <JSONL 경로>    user 프롬프트를 [번호] 목록으로 출력
필터는 전부 코드다 — LLM 판단 없음. 토큰 0.
"""
import argparse, glob, json, os, time

SKIP_MARKERS = ("<command-name>", "<local-command-stdout>", "<task-notification>",
                "<bash-input>", "<bash-stdout>")
SKIP_PREFIXES = (
    "[Request interrupted by user",
    "This session is being continued from a previous conversation",
)
MIN_LEN = 10      # 미만 = 맞장구("ㅇㅇ 해") → 제외
TRUNC = 500       # 초과분 절단
WARN_COUNT = 40   # 초과 시 경고 → 스킬이 범위를 물어야 함


def user_texts(path):
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
        out.append(txt)
    # 연속 재전송 dedup: 직전 항목이 현재 항목의 접두면 직전 것을 버린다
    deduped = []
    for t in out:
        if deduped and t.startswith(deduped[-1]):
            deduped.pop()
        deduped.append(t)
    return deduped


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
    a = ap.parse_args()
    if a.list or not a.session:
        cmd_list()
        return
    prompts = user_texts(a.session)
    if len(prompts) > WARN_COUNT:
        print(f"⚠️ 프롬프트 {len(prompts)}개 — 채점 전에 범위를 좁혀라 (예: 최근 N개)\n")
    for i, t in enumerate(prompts, 1):
        if len(t) > TRUNC:
            t = t[:TRUNC] + " …[절단됨]"
        print(f"[{i}] " + t.replace("\n", " ⏎ "))
        print()


if __name__ == "__main__":
    main()
