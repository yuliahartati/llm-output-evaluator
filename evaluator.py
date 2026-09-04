from openai import OpenAI

from rubrics import SYSTEM_PROMPT


class LLMOutputEvaluator:

    def __init__(self, api_key):

        self.client = OpenAI(api_key=api_key)

    def evaluate(self, user_prompt, llm_output):

        evaluation_prompt = f"""
User Prompt:

{user_prompt}

----------------------------------------

LLM Output:

{llm_output}
"""

        response = self.client.chat.completions.create(
            model="gpt-5-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": evaluation_prompt
                }
            ]
        )

        return response.choices[0].message.content
