# AI Startup Due Diligence Assistant

## Overview
AI Startup Due Diligence Assistant is a Generative AI-powered platform designed to automate the preliminary startup evaluation process.

The application enables users to upload startup pitch decks in PDF format and automatically generates structured investment insights including startup summaries, business model analysis, competitor analysis, risk assessment, and investment recommendations.

The project was inspired by my experience as Investment Analyst at India Accelerator, where startup screening and preliminary due diligence formed a critical part of the investment evaluation workflow.

## Project Workflow
- Upload Startup Pitch Deck
- Extract Text from PDF
- Process Startup Information using Gemini AI
- Generate Due Diligence Report
- Display Investment Insights and Recommendations

### Features
- Upload startup pitch deck PDFs
- Extract startup information
- Generate startup summaries
- Competitor analysis
- Risk assessment
- Investment recommendation
- Startup scoring

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- PyPDF2

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Sample Report Output
The platform automatically generates:
- Startup Summary
- Problem Being Solved
- Business Model
- Target Customers
- Market Opportunity
- Competitor Analysis
- Key Strengths
- Key Risks
- Investment Recommendation
- Startup Score (Out of 10)

## Impact
- Reduced preliminary startup screening effort through automated report generation.
- Accelerated first-level due diligence by providing structured investment insights.
- Improved efficiency of startup evaluation workflows.
