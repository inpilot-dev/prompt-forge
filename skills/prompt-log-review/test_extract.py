"""extract.py 필터 테스트 — 픽스처는 실세션에서 관찰된 레코드 유형 전부를 흉내낸다."""
import json, subprocess, sys, tempfile, os

HERE = os.path.dirname(os.path.abspath(__file__))

def _rec(txt, **kw):
    o = {"type": "user", "message": {"content": txt}}
    o.update(kw)
    return o

RECORDS = [
    _rec("백테스트 결과 분석해줘. 데이터는 위에 붙였어."),                # 1: 정상 → 남음
    _rec("ㅇㅇ 해"),                                                      # 2: 5자 미만 → 제외
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
    """정확히 4자는 제외, 정확히 5자는 포함."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("a" * 4), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec("b" * 5), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert len(lines) == 1, lines
    assert lines[0] == "[1] " + "b" * 5

def test_short_korean_command_survives():
    """MIN_LEN 5 하향 회귀 방지: 6자 진짜 명령("다시 진행해")은 남고,
    3~4자 맞장구("그래용"/"ㅇㅇ 해")는 여전히 빠진다."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("다시 진행해"), ensure_ascii=False) + "\n")  # 6자 → 남음
        f.write(json.dumps(_rec("그래용"), ensure_ascii=False) + "\n")       # 3자 → 제외
        f.write(json.dumps(_rec("ㅇㅇ 해"), ensure_ascii=False) + "\n")      # 4자 → 제외
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert len(lines) == 1, lines
    assert lines[0] == "[1] 다시 진행해"
    assert "그래용" not in out
    assert "ㅇㅇ 해" not in out

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

def test_bash_envelope_excluded():
    """인라인 배시모드 봉투(<bash-input>/<bash-stdout>)는 시스템 주입이라 제외되어야 한다."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("<bash-input>ls -la</bash-input>"), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec("<bash-stdout>output</bash-stdout>"), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec("정상 프롬프트는 살아있어야 한다"), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    assert "<bash-input>" not in out
    assert "<bash-stdout>" not in out
    assert "정상 프롬프트는 살아있어야 한다" in out

def test_interrupt_marker_excluded():
    """Claude Code가 삽입하는 중단 마커(`<`로 시작하지 않음)는 제외되어야 한다."""
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec("[Request interrupted by user for tool use]"), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert len(lines) == 0, lines

def test_compaction_preamble_excluded():
    """컨텍스트 자동압축 이어붙이기 서문(`<`로 시작하지 않음)은 제외되어야 한다."""
    txt = ("This session is being continued from a previous conversation "
           "that ran out of context. The summary" + " lorem ipsum" * 40)
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec(txt), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    assert "This session is being continued" not in out

def test_skip_prefix_mention_survives():
    """SKIP_PREFIXES 문구를 중간에 언급만 하는 정상 프롬프트는 살아남아야 한다(접두 검사라 부분매치로 안 삼켜짐)."""
    txt1 = "압축 서문 This session is being continued from a previous conversation 이게 왜 섞이는지 봐줘"
    txt2 = "extract.py가 <bash-input> 봉투도 걸러야 하나?"
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec(txt1), ensure_ascii=False) + "\n")
        f.write(json.dumps(_rec(txt2), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    assert txt1 in out
    assert txt2 in out

def test_warn_count_threshold():
    """WARN_COUNT 경계 고정: 40개는 경고 없음, 41개는 첫 줄이 ⚠️로 시작."""
    def _build(n):
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                         encoding="utf-8") as f:
            for i in range(n):
                f.write(json.dumps(_rec(f"프롬프트 채우기용 열자이상 텍스트 {i}"),
                                    ensure_ascii=False) + "\n")
            return f.name
    path40 = _build(40)
    out40 = run_extract(path40)
    os.unlink(path40)
    assert not out40.splitlines()[0].startswith("⚠️"), out40.splitlines()[0]

    path41 = _build(41)
    out41 = run_extract(path41)
    os.unlink(path41)
    assert out41.splitlines()[0].startswith("⚠️"), out41.splitlines()[0]

def test_newline_flattened():
    """본문 중간 개행이 출력에서 ' ⏎ '로 평탄화된다(SKILL.md는 한 항목=한 줄을 전제)."""
    txt = "여러 줄로 붙여넣은 텍스트\n두 번째 줄\n세 번째 줄"
    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False,
                                     encoding="utf-8") as f:
        f.write(json.dumps(_rec(txt), ensure_ascii=False) + "\n")
        path = f.name
    out = run_extract(path)
    os.unlink(path)
    lines = [l for l in out.splitlines() if l.startswith("[")]
    assert len(lines) == 1, lines
    assert lines[0] == "[1] 여러 줄로 붙여넣은 텍스트 ⏎ 두 번째 줄 ⏎ 세 번째 줄"

if __name__ == "__main__":
    test_filters()
    test_truncation_length()
    test_tag_mention_survives()
    test_non_object_json_line_tolerated()
    test_min_len_boundary()
    test_short_korean_command_survives()
    test_trunc_boundary()
    test_bash_envelope_excluded()
    test_interrupt_marker_excluded()
    test_compaction_preamble_excluded()
    test_skip_prefix_mention_survives()
    test_warn_count_threshold()
    test_newline_flattened()
    print("ok")
