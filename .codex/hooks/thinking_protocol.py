import json

message = (
    "本轮内化执行四步思考协议，不输出标签：\n"
    "1. 分析：明确任务、标准、词义边界。\n"
    "2. 检索：需要事实、文献、最新状态或文件证据时先查。\n"
    "3. 推导：先看反例和断点，再收敛判断。\n"
    "4. 执行：路径清楚后动手；遇到新不确定性回到推导。"
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": message,
    }
}, ensure_ascii=False))
