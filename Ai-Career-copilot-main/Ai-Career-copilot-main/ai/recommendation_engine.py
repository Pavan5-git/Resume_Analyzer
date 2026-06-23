import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_recommendations(resume, jd):

    prompt = f"""
Analyze this resume and job description.

Give:
1. Missing skills
2. Resume improvements
3. Recommended projects

Resume:
{resume}

Job Description:
{jd}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response.choices[0].message.content

    return {
        "missing_skills": ["AI Generated"],
        "improvements": text,
        "projects": text
    }