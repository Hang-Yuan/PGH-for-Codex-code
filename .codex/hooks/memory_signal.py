import json

message = (
    "每条用户输入后，基于 Schema Prediction 判本次观察两轴：\n"
    "- P 轴（预测偏差）：命中 / 击穿 / 未覆盖\n"
    "- C 轴（情绪校准信号）：正向确认 / 反对 / 纠正 / 中性\n"
    "除 P=命中 且 C=中性 外均值得记。若达到写入下限，用本地文件编辑工具追加一行到 "
    "<ASSISTANT_ROOT>/MEMORY/episodic_inbox.md。细则按需读取 MEMORY/00.记忆区_agent.md §两轴判定。"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": message,
    }
}, ensure_ascii=False))
