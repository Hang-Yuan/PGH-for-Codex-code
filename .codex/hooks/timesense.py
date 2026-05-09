import datetime
import json

weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
now = datetime.datetime.now().astimezone()
value = f"{now:%Y-%m-%d %H:%M} {weekdays[now.weekday()]}"
message = (
    "当前时间：{0}。只在最终面向用户的回复时，第一行按此格式输出"
    "（反引号包裹的 inline code，单行，不加任何前后缀）：`{0}`。"
    "工具调用过程中的中间回复不输出时间戳。"
).format(value)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": message,
    }
}, ensure_ascii=False))
