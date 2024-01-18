
import re
import pdfplumber

def extract_skills_and_experience(resume_path):
    SKILLS_PATTERN = r"(Skills|Technical Skills|Proficiencies):\s*(.+)"
    EXPERIENCE_PATTERN = r"(Experience|Work Experience|Professional Experience):\s*(.+)"

    skills = []
    experience = []

    with pdfplumber.open(resume_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                skills_match = re.search(SKILLS_PATTERN, line, re.IGNORECASE)
                experience_match = re.search(EXPERIENCE_PATTERN, line, re.IGNORECASE)
                if skills_match:
                    skills.extend([s.strip() for s in skills_match.group(2).split(',')])
                if experience_match:
                    experience.append(experience_match.group(2).strip())

    return skills, experience
