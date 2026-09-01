#!/bin/zsh
# weekly-review.sh — 주 1회 자동 세션 채점 (ledger 축적 → 최약축 추이 데이터).
# launchd(월 10:17, 잠자면 깨어날 때 실행)가 부른다. 설치는 SKILL.md '주간 자동 실행' 참조.
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"

PICK="$(python3 "$SKILL_DIR/extract.py" --pick)"
if [ -z "$PICK" ]; then
  echo "$(date '+%F %T') 지난 7일 채점할 세션 없음"
  exit 0
fi
echo "$(date '+%F %T') 채점 대상: $PICK"

# 40개 게이트·워커 판정의 답을 프롬프트에 선지급한다 (headless라 물을 수 없음)
claude -p "/prompt-log-review $PICK — 주간 자동 실행이다: 프롬프트가 40개를 넘으면 묻지 말고 최근 40개만 채점하고, 워커·디스패치 세션으로 판정되면 채점하지 말고 사유만 출력하고 끝내라." \
  --allowedTools "Bash(python3:*)" "Read" "Edit" "Write"
echo "$(date '+%F %T') 완료 (exit $?)"
