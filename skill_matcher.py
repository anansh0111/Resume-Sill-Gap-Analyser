def extract_skills(text, skill_list):
    text = text.lower()
    return [skill for skill in skill_list if skill.lower() in text]

def compute_skill_gap(resume_skills, jd_skills):
    matched = set(resume_skills) & set(jd_skills)
    missing = set(jd_skills) - set(resume_skills)
    score = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0
    return matched, missing, score
