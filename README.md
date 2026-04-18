# 🤖 Multi-Agent Job Application Bot

A 3-agent AI system built with CrewAI that automates the job application process — Resume Analyzer, Job Matcher, and Cover Letter Generator working together autonomously.

🔴 **Live Demo**: [huggingface.co/spaces/nitz0219/job-application-bot](https://nitz0219-job-application-bot-v1.hf.space)

---

## 🧠 What It Does

Input a job description → 3 specialized AI agents collaborate → Get a tailored cover letter + resume match analysis + application strategy.

---

## 🏗️ Multi-Agent Architecture

```
Job Description Input
        ↓
┌─────────────────────────────────┐
│         CrewAI Orchestrator     │
└─────────────────────────────────┘
        ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Agent 1    │  │   Agent 2    │  │   Agent 3    │
│   Resume     │→ │    Job       │→ │   Cover      │
│   Analyzer   │  │   Matcher    │  │   Letter     │
│              │  │              │  │   Generator  │
└──────────────┘  └──────────────┘  └──────────────┘
        ↓
  Final Output:
  - Match Score
  - Gap Analysis  
  - Tailored Cover Letter
  - Application Strategy
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Agent Framework | CrewAI |
| LLM Orchestration | LangChain + LangGraph |
| LLM | OpenAI GPT-4o |
| Backend | FastAPI |
| Database | SQLite |
| Deployment | Docker + Hugging Face Spaces |

---

## 🚀 System Design Features

- **Multi-Agent Orchestration** — agents work sequentially, passing context
- **LangGraph Workflow** — structured agent communication
- **Database Integration** — saves every application for history
- **Docker** — fully containerized deployment

---

## 👨‍💻 Author

**Nitesh Nankani** — AI/ML Engineer  
[HuggingFace](https://huggingface.co/nitz0219) | [GitHub](https://github.com/niteshnankani-svg) | [LinkedIn](https://linkedin.com/in/niteshnankani)
