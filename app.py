import streamlit as st

from evaluator import LLMOutputEvaluator
from utils import (
    parse_response,
    build_markdown_report,
    score_color,
    overall_label
)

st.set_page_config(
    page_title="LLM Output Evaluator",
    page_icon="📊",
    layout="wide"
)

st.title("📊 LLM Output Evaluator")

st.write(
    "Evaluate AI-generated responses using a structured quality rubric."
)

api_key = st.secrets.get("OPENAI_API_KEY", None)

if not api_key:
    st.error("OPENAI_API_KEY not found.")
    st.stop()

evaluator = LLMOutputEvaluator(api_key)

user_prompt = st.text_area(
    "Original User Prompt",
    height=150
)

llm_output = st.text_area(
    "LLM Output",
    height=300
)

if st.button("📊 Evaluate"):

    if not user_prompt.strip():

        st.warning("Please enter the original prompt.")
        st.stop()

    if not llm_output.strip():

        st.warning("Please enter the LLM output.")
        st.stop()

    with st.spinner("Evaluating..."):

        result_json = evaluator.evaluate(
            user_prompt,
            llm_output
        )

    try:

        result = parse_response(result_json)

        st.success("Evaluation completed!")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Overall Score",
                f"{result['overall_score']}/100"
            )

        with col2:

            st.metric(
                "Quality",
                overall_label(result["overall_score"])
            )

        st.info(result["summary"])

        for item in result["criteria"]:

            icon = score_color(item["score"])

            with st.expander(
                f"{icon} {item['name']} ({item['score']}/100)"
            ):

                st.markdown("### Feedback")

                st.write(item["feedback"])

                st.markdown("### Suggestions")

                if item["suggestions"]:

                    for suggestion in item["suggestions"]:

                        st.markdown(f"- {suggestion}")

                else:

                    st.success("No suggestions.")

        report = build_markdown_report(result)

        st.download_button(
            "📄 Download Markdown Report",
            report,
            file_name="llm_output_evaluation.md",
            mime="text/markdown"
        )

    except Exception:

        st.error("Model did not return valid JSON.")

        st.code(result_json)
