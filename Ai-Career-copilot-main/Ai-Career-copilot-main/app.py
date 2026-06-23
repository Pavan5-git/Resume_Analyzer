import streamlit as st
from ai.resume_parser import extract_text_from_pdf
from ai.semantic_match import calculate_similarity
from ai.recommendation_engine import generate_recommendations

st.set_page_config(page_title="AI Career Copilot")

st.title("🚀 AI Career Copilot")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        with st.spinner("Analyzing resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            score = calculate_similarity(
                resume_text,
                job_description
            )

            result = generate_recommendations(
                resume_text,
                job_description
            )

        st.subheader("🎯 Match Score")

        score = int(score)

        st.progress(score)

        st.success(f"{score}% Match")

        st.subheader("❌ Missing Skills")

        for skill in result["missing_skills"]:
            st.write(f"- {skill}")

        st.subheader("🛠 Resume Improvements")

        st.write(result["improvements"])

        st.subheader("📚 Recommended Projects")

        st.write(result["projects"])

    else:

        st.warning(
            "Please upload resume and enter job description."
        )