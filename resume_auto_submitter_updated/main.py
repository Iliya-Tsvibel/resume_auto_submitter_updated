
from resume_parser import extract_skills_and_experience
from job_scraper import scrape_job_listings
from ai_matcher import match_jobs_to_skills

# Example usage
resume_path = 'path/to/your/resume.pdf'
skills, experience = extract_skills_and_experience(resume_path)

skill = 'Python Developer'  # Example skill to scrape jobs
scraped_jobs = scrape_job_listings(skill)
matched_jobs = match_jobs_to_skills(scraped_jobs, skills)

# Print the top 5 matched jobs
for job in matched_jobs[:5]:
    print(job)
