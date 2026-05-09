import json
import re
import sys

raw_input = sys.stdin.read()
try:
    payload = json.loads(raw_input) if raw_input.strip() else {}
except json.JSONDecodeError:
    payload = {}

prompt = str(payload.get("prompt", raw_input))
pattern = re.compile(r"(晚安|今天就到这里|今天先到这里|bye|good night|that's all for today)", re.IGNORECASE)
if not pattern.search(prompt):
    sys.exit(0)

message = (
    "用户触发了会话收束语。先执行 daily-review skill：消耗 episodic_inbox，更新必要的 "
    "episodic_memory / MEMORY_LOG / 本周进展；完成后再回应告别。"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": message,
    }
}, ensure_ascii=False))
