import json

message = (
    "每轮内化判断两点（不主动展开，触发到才问）：\n"
    "1. 本轮像阶段性收尾或子问题闭合：询问是否执行 close-node 整理。\n"
    "2. 本轮明显进入某具体项目，但尚未项目加载：询问是否在该项目下工作；确认后读取项目 _overview.md。"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": message,
    }
}, ensure_ascii=False))
