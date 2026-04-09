# 🚀 PatchPulse – AI-Powered Code Review Agent

PatchPulse is an intelligent code review agent that automates pull request (PR) analysis using LLMs. It fetches code changes from GitHub, performs semantic analysis, and posts AI-generated review comments directly on PRs.

---

## ✨ Features

- 🔍 Extracts code changes from GitHub PR URLs  
- 🤖 AI-powered code review using LLMs  
- 🧠 Semantic search with Qdrant vector database  
- 💬 Automatically posts review comments on PRs  
- ⚡ End-to-end automated review workflow  

---

---

## 🛠️ Tech Stack

- **Backend**: FastAPI  
- **Frontend**: Streamlit  
- **LLM**: OpenAI / Groq  
- **Vector DB**: Qdrant  
- **APIs**: GitHub REST API  
- **Language**: Python  

---

## ⚙️ How It Works

1. User provides a GitHub PR URL  
2. System extracts owner, repo, PR number  
3. Fetches file diffs using GitHub API  
4. Processes and converts code changes into embeddings  
5. Stores embeddings in Qdrant  
6. Retrieves relevant context  
7. Generates AI-based code review  
8. Posts comments back to the PR  

---

## 📦 Installation

```bash
git clone https://github.com/your-username/patchpulse.git
cd patchpulse
pip install -r requirements.txt
```
## 📦 How to run
```bash
streamlit run app/main.py
```
