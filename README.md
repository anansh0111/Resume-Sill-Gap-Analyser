# 💼 SkillFit – Resume Skill Gap Analyzer

SkillFit is a Streamlit-based application that helps job seekers compare their resume against a job description, identify skill gaps, and get personalized course recommendations to upskill.

---

## 🚀 Features

- 📄 Upload your resume (PDF format)
- 📝 Paste a job description
- ⚙️ Extract and compare skills using basic NLP
- 📊 View a skill match score
- ❌ Get a list of missing skills
- 🎯 Receive recommended online courses to bridge the gap

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – Frontend UI
- **PyMuPDF** –

## 📁 Project Structure
skillfit/
├── app.py # Main Streamlit application
├── resume_parser.py # PDF text extraction from resumes
├── jd_parser.py # Job description text cleaning
├── skill_matcher.py # Skill comparison & scoring
├── course_recommender.py # Online course recommendations
├── requirements.txt # Python dependencies
├── README.md # This file
└── sample_data/
└── skill_list.py # A simple hardcoded list of in-demand skills
