import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import extract_text_from_jd
from skill_matcher import extract_skills, compute_skill_gap
from course_recommender import recommend_courses
from sample_data.skill_list import skill_list

st.set_page_config(page_title="SkillFit - Resume Skill Gap Analyzer", layout="centered")
st.title("📄 SkillFit - Resume Skill Gap Analyzer")
st.markdown("""
Easily compare your resume against a job description to find missing skills and improve your chances of getting hired.
""")

resume_file = st.file_uploader("**Upload Resume (PDF)**", type=["pdf"])
jd_input = st.text_area("**Paste Job Description Here**")

if st.button("🔍 Analyze"): 
    if resume_file and jd_input:
        resume_text = extract_text_from_pdf(resume_file)
        jd_text = extract_text_from_jd(jd_input)

        resume_skills = extract_skills(resume_text, skill_list)
        jd_skills = extract_skills(jd_text, skill_list)

        matched, missing, score = compute_skill_gap(resume_skills, jd_skills)
        recommendations = recommend_courses(missing)

        st.markdown(f"### ✅ Skill Match Score: **{score}%**")
        st.success(f"Matched Skills: {', '.join(matched) if matched else 'None'}")
        st.warning(f"Missing Skills: {', '.join(missing) if missing else 'None'}")

        st.markdown("### 🎯 Recommended Courses:")
        for skill, link in recommendations.items():
            st.markdown(f"- **{skill.title()}**: [Course Link]({link})")
    else:
        st.error("Please upload a resume and paste a job description.")
