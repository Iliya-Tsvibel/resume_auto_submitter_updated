
def match_jobs_to_skills(job_listings, skills):
    matched_jobs = []

    for job in job_listings:
        job_title = job['title'].lower()
        job_company = job['company'].lower()

        matches = sum(skill.lower() in job_title or skill.lower() in job_company for skill in skills)

        job['matches'] = matches
        matched_jobs.append(job)

    matched_jobs.sort(key=lambda x: x['matches'], reverse=True)
    matched_jobs = [job for job in matched_jobs if job['matches'] > 0]

    return matched_jobs
