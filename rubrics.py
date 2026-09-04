RUBRICS = [
    {
        "name": "Accuracy",
        "description": "Evaluate whether the response is factually correct and free from misinformation."
    },
    {
        "name": "Completeness",
        "description": "Evaluate whether the response fully addresses the user's request."
    },
    {
        "name": "Clarity",
        "description": "Evaluate whether the response is easy to understand, well-written, and free from ambiguity."
    },
    {
        "name": "Relevance",
        "description": "Evaluate whether the response stays focused on the user's request without unnecessary information."
    },
    {
        "name": "Logical Consistency",
        "description": "Evaluate whether the reasoning is internally consistent and free from contradictions."
    },
    {
        "name": "Structure",
        "description": "Evaluate whether the response is organized with a logical flow and appropriate formatting."
    },
    {
        "name": "Hallucination Risk",
        "description": "Estimate the likelihood that unsupported or fabricated information is present."
    },
    {
        "name": "Actionability",
        "description": "Evaluate whether the response provides useful, practical, and actionable guidance."
    }
]

SYSTEM_PROMPT = """
You are an expert evaluator of Large Language Model (LLM) outputs.

Evaluate the provided AI-generated response using the rubric below.

For each criterion:
- Assign a score from 0 to 100.
- Explain the reasoning briefly.
- Suggest one or more improvements when appropriate.

Return ONLY valid JSON using this schema:

{
  "overall_score": 0,
  "summary": "",
  "criteria": [
    {
      "name": "",
      "score": 0,
      "feedback": "",
      "suggestions": []
    }
  ]
}
"""
