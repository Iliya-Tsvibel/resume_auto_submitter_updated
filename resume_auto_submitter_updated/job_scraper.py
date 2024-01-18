
from bs4 import BeautifulSoup
import requests

def scrape_job_listings(skill, location='United States', site='Indeed'):
    URL_TEMPLATE = "https://www.indeed.com/jobs?q={skill}&l={location}"
    url = URL_TEMPLATE.format(skill=skill.replace(' ', '+'), location=location.replace(' ', '+'))

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = []

    for job_card in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job_card.find('h2', class_='title').text.strip()
        company = job_card.find('span', class_='company').text.strip()
        job_link = 'https://www.indeed.com' + job_card.find('a')['href']

        job_listings.append({
            'title': title,
            'company': company,
            'link': job_link
        })

    return job_listings
