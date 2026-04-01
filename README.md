# 🤖 Job Application Bot

An AI-powered job application assistant built with CrewAI and Streamlit.

## What It Does

Upload your Job Description and Resume → Get instant analysis and a personalized cover letter.

## Features

- 📄 Analyzes Job Description and extracts top requirements
- 👤 Analyzes your Resume and extracts key skills
- 🎯 Matches your profile against job requirements
- ✉️ Generates a personalized cover letter
- 📥 Download your cover letter instantly

## How To Use

1. Enter your OpenAI API key
2. Upload Job Description PDF
3. Upload Resume PDF
4. Click Analyze & Generate Cover Letter
5. View results in tabs
6. Download your cover letter

## Built With

- CrewAI - Multi agent framework
- Streamlit - UI framework
- OpenAI - LLM engine
- PyPDF - PDF reading

## Project Structure
```
job-application-bot/
├── app.py              ← CrewAI agents and logic
├── streamlit_app.py    ← Streamlit UI
├── requirements.txt    ← Python dependencies
└── README.md           ← Project documentation
```

## Author

Nitesh Nankani - AI/ML Engineer
```

---

Also create `runtime.txt` with just this inside:
```
3.12
```

This tells Streamlit Cloud to use Python 3.12. 🎯

Your folder should now have:
```
job-application-bot/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── runtime.txt
└── README.md
