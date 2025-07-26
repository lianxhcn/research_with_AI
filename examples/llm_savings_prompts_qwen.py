# 文件：llm_savings_prompts_qwen.py

# -----------------------------
# 1. 中文题库设计（共 14 题）
# -----------------------------

questions = [
    # 时间偏好
    "假设你现在可以获得 1,000 元，或者等待 1 年获得 X 元。请问，X 至少是多少，才能让你愿意等待一年？",
    "假设你可以立刻获得 2,000 元，或者在 10 年后获得 Y 元。请问，Y 至少是多少，才能让你愿意等待？",

    # 收入分配
    "如果你的下月工资多出 2,000 元，你会如何分配这笔钱？请用百分比表示：食品 __%、娱乐 __%、教育 __%、储蓄 __%。",
    "如果你的收入减少 1,000 元，你最可能减少哪一项支出？A. 食品 B. 教育 C. 娱乐 D. 储蓄。请简要说明理由。",

    # 预防性储蓄
    "假设你得知你父亲未来一年可能需要 10,000 元医疗支出，你是否会调整当前的消费？你愿意每月减少多少元用于储蓄？",
    "你是否有每月固定的预防性储蓄计划（如应对失业、健康支出）？如有，请简要说明金额与动机。",

    # 风险认知与应对
    "假设你所在行业未来一年有 10% 的失业概率，你是否会因此增加储蓄？若会，预计增加多少元/月？",
    "假设某保险产品年保费 800 元，可覆盖重大疾病 30 万元赔偿。你是否愿意购买？请说明理由。",

    # 家庭生命周期
    "你是否因为孩子的教育而主动减少自己的日常消费？请列举最近一次这样的决策和金额。",
    "如果你刚生育一个孩子，你会如何调整以下支出比例（教育 __%、娱乐 __%、储蓄 __%、其他 __%）？",

    # 消费偏好
    "请列举你最近三个月最大的一笔消费支出，并说明其动因（如：必要/非必要、情绪驱动、家庭责任等）。",
    "在没有收入压力的前提下，你更倾向于提前消费还是储蓄？请简要说明原因。",

    # 财富认知
    "你认为一个家庭是否有必要维持至少 6 个月的生活费作为紧急储备？为什么？",
    "你认为影响储蓄倾向最重要的因素是什么？A. 收入 B. 教育水平 C. 风险意识 D. 家庭责任感。请说明理由。"
]

# -----------------------------
# 2. 标准化 Prompt 模板（支持通义千问）
# -----------------------------

prompt_template = """
以下是一个关于中国家庭储蓄与消费决策的情境问题。
请根据你的判断，独立作答。

问题：{question}

请只输出你的答案，不需要解释或重复题干。
如果涉及金额，请直接给出数字或百分比。
"""

def build_prompts(questions):
    prompts = []
    for q in questions:
        prompts.append(prompt_template.format(question=q))
    return prompts


# -----------------------------
# 3. 伪代码：通义千问版本的实验流程
# -----------------------------

"""
1. 读取题库，构造 prompts
2. 设置通义 dashscope API 的参数（如模型 qwen-plus）
3. 每题生成 n_repeat 次回答
4. 所有回答结果保存为 CSV
5. 可选：记录响应时间、异常处理信息
"""

# -----------------------------
# 4. 通义千问实操代码（DashScope API）
# -----------------------------

import dashscope
import time
import pandas as pd

# 替换为你的通义 API Key
DASHSCOPE_API_KEY = "YOUR_DASHSCOPE_API_KEY"
dashscope.api_key = DASHSCOPE_API_KEY

# 构建 prompts
prompts = build_prompts(questions)

model_name = "qwen-plus"
n_repeat = 100

data = []

for qid, prompt in enumerate(prompts):
    for trial in range(n_repeat):
        try:
            response = dashscope.Generation.call(
                model=model_name,
                prompt=prompt,
                temperature=0.7,
                top_p=0.9,
                result_format="message"
            )
            answer = response.output.choices[0].message.content.strip()
            data.append({
                "question_id": qid + 1,
                "trial": trial + 1,
                "response": answer
            })
            time.sleep(0.3)  # 限速保护
        except Exception as e:
            print(f"错误：Q{qid+1}-T{trial+1}: {e}")
            time.sleep(2)

# 保存为 CSV
pd.DataFrame(data).to_csv("qwen_savings_responses.csv", index=False)
print("实验完成，结果已保存。")
