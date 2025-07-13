course_db = {
    "python": "https://www.coursera.org/learn/python",
    "sql": "https://www.udemy.com/course/sql-for-beginners/",
    "data analysis": "https://www.datacamp.com/courses/data-analysis",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "communication": "https://www.udemy.com/course/communication-skills/",
    "project management": "https://www.edx.org/learn/project-management"
}
def recommend_courses(missing_skills):
    return {skill: course_db.get(skill.lower(), "https://www.google.com/search?q=" + skill + "+course") for skill in missing_skills}

