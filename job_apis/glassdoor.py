import requests
import pprint
import bs4
import subprocess
import json
import csv
import datetime
from tqdm import tqdm


def request_searchUrl(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GDApple/9.1.0',
        # 'Referer': 'https://api.glassdoor.com/api-internal/api.htm?responseType=json&t.p=16&t.k=fz6JLNgLgVs&version=1.2&pageNumber=1&locId=1140177&locT=C&keyword=Lab&action=jobs&s.expires=1648595117724&signature=ucda5nWj%2BiLfPPtQvXRFHNIrTCo%3D&locale=en_US&deviceLocale=en_US&gdAppVersion=9.1.0',
    }
    params = {
        'responseType': 'json',
        't.p': '16',
        't.k': 'fz6JLNgLgVs',
        'version': '1.2',
        'pageNumber': '1',
        'locId': '1140177',
        'locT': 'C',
        'keyword': '{}'.format(keyword),
        'action': 'jobs',
        's.expires': '1648595117724',
        'signature': 'ucda5nWj+iLfPPtQvXRFHNIrTCo=',
        'locale': 'en_US',
        'deviceLocale': 'en_US',
        'gdAppVersion': '9.1.0',
    }

    response = requests.get('https://api.glassdoor.com/api-internal/api.htm', headers=headers, params=params)
    attributionURL = response.json()['response']['attributionURL']
    return attributionURL


def add_job_to_list(job_url,api):
    with open("job_url.html") as fp:
        soup = bs4.BeautifulSoup(fp, "html.parser")
        json_data = soup.find("script", {"type": "application/ld+json"})
        data = json.loads(json_data.string)
        # description = data['description']
        datePosted = data['datePosted']
        company = data['hiringOrganization']['name']
        datePosted = datetime.datetime.strptime(datePosted, '%Y-%m-%dT%H:%M:%S').strftime('%b %d, %Y')
        with open('jobfilter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([company, datePosted,job_url,api])

        # return job_url





def glassdoor_api(keyword):
    api = "glassdoor"
    attributionURL = request_searchUrl(keyword)
    proc = subprocess.Popen(["curl", "-o", "glassdoor_jobs.html", attributionURL], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    with open("glassdoor_jobs.html") as fp:
        soup = bs4.BeautifulSoup(fp, "html.parser")
        json_data = soup.find("script", {"type": "application/ld+json"})
        data = json.loads(json_data.string)
        jobs = data['itemListElement']
        for job in jobs:
            job_url = job['url']
            proc = subprocess.Popen(["curl", "-o", "job_url.html", job_url], stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            add_job_to_list(job_url,api)

