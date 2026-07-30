"""extract.py 필터 테스트 — 픽스처는 실세션에서 관찰된 레코드 유형 전부를 흉내낸다."""
import json, subprocess, sys, tempfile, os

HERE = os.path.dirname(os.path.abspath(__file__))

def _rec(txt, **kw):
    o = {"type": "user", "message": {"content": txt}}
    o.update(kw)
    return o

RECORDS = [
    _rec("백테스트 결과 분석해줘. 데이터는 위에 붙였어."),                # 1: 정상 → 남음
    _rec("ㅇㅇ 해"),                                                      # 2: 10자 미만 → 제외
    {"type": "assistant", "message": {"content": "답변"}},                 # 3: user 아님 → 제외
    _rec("<command-message>forge-run</command-message>\n<command-name>/forge-run</command-name> 긴 커맨드 본문"),  # 4: 커맨드 → 제외
    _rec("<local-command-stdout>Set model to Fable</local-command-stdout> 그리고 부가 텍스트"),  # 5: stdout → 제외
    _rec("<task-notification>\n<task-id>abc</task-id>\n</task-notification> 결과 요약"),  # 6: 태스크알림 → 제외
    _rec("[Image: source: 스크린샷.png] 이미지 메타인데 길이는 충분히 길다", isMeta=True),  # 7: isMeta → 제외
    _rec("사이드체인 서브에이전트 프롬프트라 길이는 충분", isSidechain=True),  # 8: isSidechain → 제외
    # 9: tool_result만 있는 리스트 콘텐츠 → 제외
    {"type": "user", "message": {"content": [{"type": "tool_result", "content": "결과"}]}},
    # 10: 리스트 콘텐츠지만 text 블록 있음 → 남음
    {"type": "user", "message": {"content": [{"type": "text", "text": "리스트 형태로 온 진짜 프롬프트다"}]}},
    # 11+12: 재전송 dedup — 앞이 뒤의 접두 → 앞 것 버리고 뒤만 남음
    _rec("스킬 말한거였어 그리고 궁금한게 있는데"),
    _rec("스킬 말한거였어 그리고 궁금한게 있는데 patterns 파일도 있을까?"),
    # 13: 500자 초과 → 절단 표시
    _rec("긴 붙여넣기 " + "x" * 600),
]

def run_extract(path):
    r = subprocess.run([sys.executable, os.path.join(HERE, "extract.py"), path],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout

def test_filters():
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        for rec in RECORDS:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    # 남아야 할 것
    assert "백테스트 결과 분석해줘" in out
    assert "리스트 형태로 온 진짜 프롬프트다" in out
    assert "patterns 파일도 있을까?" in out          # dedup: 긴 쪽 생존
    assert "…[절단됨]" in out                        # 절단 표시
    # 빠져야 할 것
    assert "ㅇㅇ 해" not in out
    assert "<command-name>" not in out
    assert "<local-command-stdout>" not in out
    assert "<task-notification>" not in out
    assert "이미지 메타인데" not in out               # isMeta
    assert "사이드체인" not in out                    # isSidechain
    # dedup: 접두(짧은 쪽)는 항목으로 존재하면 안 됨 — 항목 라인 형식 "[N] ..." 기준
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert not any(l.endswith("궁금한게 있는데") for l in lines)
    # 개수: 정상 4건 (1, 10, 12, 13)
    assert len(lines) == 4, lines

def test_truncation_length():
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("긴 붙여넣기 " + "y" * 600), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    body = [l for l in out.splitlines() if l.startswith("[1]")][0]
    assert len(body) == len("[1] ") + 500 + len(" …[절단됨]")

def test_tag_mention_survives():
    """태그를 언급만 하는 정상 프롬프트는 SKIP_MARKERS 부분매치로 삼켜지면 안 된다."""
    txt = "extract.py에서 <command-name> 태그를 어떻게 걸러내는지 설명해줘"
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec(txt), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    assert txt in out

def test_non_object_json_line_tolerated():
    """null 같은 비객체 유효 JSON 라인이 섞여도 프로세스가 죽지 않고 나머지는 살아남는다."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("정상 프롬프트 하나는 살아있어야 한다"), ensure_ascii=False) + "\n")
        f.write("null\n")
        f.write(json.dumps(_rec("두 번째 정상 프롬프트도 살아있어야 한다"), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)  # run_extract가 returncode 0을 내부에서 assert
    os.unlink(path)
    assert "정상 프롬프트 하나는 살아있어야 한다" in out
    assert "두 번째 정상 프롬프트도 살아있어야 한다" in out

def test_min_len_boundary():
    """정확히 9자는 제외, 정확히 10자는 포함."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("a" * 9), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec("b" * 10), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert len(lines) == 1, lines
    assert lines[0] == "[1] " + "b" * 10

def test_trunc_boundary():
    """정확히 500자는 비절단, 501자는 절단."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("c" * 500), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec("d" * 501), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert lines[0] == "[1] " + "c" * 500
    assert lines[1] == "[2] " + "d" * 500 + " …[절단됨]"

if __name__ == "__main__":
    test_filters()
    test_truncation_length()
    test_tag_mention_survives()
    test_non_object_json_line_tolerated()
    test_min_len_boundary()
    test_trunc_boundary()
    print("ok")
