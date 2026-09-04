import json


def parse_response(content):
    """
    Parse JSON returned by the model.
    """

    return json.loads(content)


def build_markdown_report(result):
    """
    Convert evaluation result into a Markdown report.
    """

    report = "# LLM Output Evaluation Report\n\n"

    report += f"## Overall Score\n\n"
    report += f"{result['overall_score']}/100\n\n"

    report += "## Summary\n\n"
    report += f"{result['summary']}\n\n"

    report += "---\n\n"

    for item in result["criteria"]:

        report += f"## {item['name']}\n\n"

        report += f"**Score:** {item['score']}/100\n\n"

        report += f"**Feedback**\n\n"
        report += f"{item['feedback']}\n\n"

        report += "**Suggestions**\n\n"

        if item["suggestions"]:

            for suggestion in item["suggestions"]:
                report += f"- {suggestion}\n"

        else:
            report += "- None\n"

        report += "\n"

    return report


def score_color(score):
    """
    Return emoji based on score.
    """

    if score >= 85:
        return "🟢"

    if score >= 70:
        return "🟡"

    return "🔴"


def overall_label(score):
    """
    Return qualitative label.
    """

    if score >= 90:
        return "Excellent"

    if score >= 80:
        return "Good"

    if score >= 70:
        return "Fair"

    if score >= 60:
        return "Needs Improvement"

    return "Poor"
