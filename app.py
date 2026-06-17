import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# ==========================
# GOOGLE GEMINI API KEY
# ==========================

api_key = "Add Your API_KEY"  # Get free key from https://aistudio.google.com/app/apikey
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# ==========================
# PAGE SETTINGS
# ==========================

st.set_page_config(
    page_title="AI Startup Due Diligence Assistant",
    layout="wide"
)

st.title("🚀 AI Startup Due Diligence Assistant")

st.write(
    "Upload a startup pitch deck and generate an AI-powered investment analysis report."
)

# ==========================
# FILE UPLOAD
# ==========================

uploaded_file = st.file_uploader(
    "Upload Startup Pitch Deck (PDF)",
    type=["pdf"]
)

# ==========================
# MAIN LOGIC
# ==========================

if uploaded_file:

    st.success("Pitch Deck Uploaded Successfully")

    # Read PDF

    pdf = PdfReader(uploaded_file)

    startup_text = ""

    for page in pdf.pages:

        text = page.extract_text()

        if text:
            startup_text += text

    st.subheader("Extracted Startup Information")

    st.text_area(
        "Pitch Deck Content",
        startup_text,
        height=250
    )

    # Prompt

    prompt = f"""

    You are an experienced Venture Capital Analyst.

    Analyze the startup information below.

    Generate a detailed due diligence report containing:

    1. Startup Summary

    2. Problem Being Solved

    3. Business Model

    4. Target Customers

    5. Market Opportunity

    6. Competitor Analysis

    7. Key Strengths

    8. Key Risks

    9. Investment Recommendation

    10. Startup Score out of 10

    Startup Information:

    {startup_text}

    """

    if st.button("Generate AI Report"):

        with st.spinner("Analyzing Startup..."):

            try:
                response = model.generate_content(prompt)
                report = response.text

            except Exception as e:
                st.error(f"Error generating report: {str(e)}")
                st.stop()

        st.subheader("📊 AI Due Diligence Report")

        st.write(report)

        # Save Report

        with open(
            "startup_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        st.success(
            "Report Generated Successfully"
        )
