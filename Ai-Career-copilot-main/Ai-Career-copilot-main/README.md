# 🚀 AI Career Copilot

An industry-ready AI-powered Resume Intelligence Platform that analyzes resumes against job descriptions using Semantic NLP and Generative AI.

This project helps students and job seekers understand:

* why resumes get rejected
* which skills are missing
* how well their resume matches a job role
* what improvements are needed

Built using:

* NLP
* Sentence Transformers
* FastAPI
* Streamlit
* Groq Llama 3

---

# ✨ Features

✅ Semantic ATS Match Score
✅ Resume Analysis
✅ Missing Skill Detection
✅ AI Resume Improvements
✅ AI Project Recommendations
✅ Semantic Resume Matching
✅ Generative AI Recommendations
✅ FastAPI Backend
✅ Streamlit Frontend

---

# 🧠 Technologies Used

| Technology            | Purpose            |
| --------------------- | ------------------ |
| Python                | Core Programming   |
| FastAPI               | Backend API        |
| Streamlit             | Frontend UI        |
| Sentence Transformers | Semantic NLP       |
| Scikit-learn          | Cosine Similarity  |
| Groq Llama 3          | Generative AI      |
| PyPDF2                | Resume PDF Parsing |
| Requests              | API Communication  |

---

# 🏗 Project Architecture

```text
User Uploads Resume + Job Description
                ↓
         Streamlit Frontend
                ↓
          FastAPI Backend
                ↓
         Resume PDF Parser
                ↓
     Semantic Similarity Engine
                ↓
      AI Recommendation Engine
                ↓
         ATS Match Score +
      AI Recommendations Returned
```

---

# 📂 Project Structure

```text
ai-career-copilot/
│
├── app.py
│
├── backend/
│   └── main.py
│
├── ai/
│   ├── semantic_match.py
│   ├── recommendation_engine.py
│   └── resume_parser.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Pavan5-git/Ai-Career-copilot.git
```

Go to project folder:

```bash
cd Ai-Career-copilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

Open another terminal:

```bash
python -m streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 📊 How It Works

1. User uploads resume PDF
2. Resume text is extracted using PyPDF2
3. Resume and job description are converted into semantic embeddings
4. Cosine similarity calculates ATS match score
5. Groq Llama 3 generates intelligent recommendations
6. Results displayed in Streamlit frontend

---

# 🔥 Why This Project Is Different

Traditional ATS systems:

* only check keywords
* fail to understand semantic meaning

AI Career Copilot:

* understands contextual similarity
* uses semantic embeddings
* provides AI-powered recommendations

Example:

* LSTM → Deep Learning
* YOLOv8 → Computer Vision
* Flask APIs → Deployment

---

# 📌 Future Improvements

* Multi-resume ranking
* Resume analytics dashboard
* Docker deployment
* Authentication system
* Database integration
* Cloud deployment
* Recruiter dashboard

---

# 👨‍💻 Author

Cherukupalli Pavan

Passionate about:

* Machine Learning
* NLP
* Generative AI
* Data Analytics
* AI Product Development

GitHub:
https://github.com/Pavan5-git

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🚀 Connect and collaborate
