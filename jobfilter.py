from job_apis import ziprecruiter
from job_apis import glassdoor
import pprint
import csv
import shutil
import os 


# remove the old csv file
if os.path.exists('jobfilter.csv'):
    os.remove('jobfilter.csv')

def cleanUp():
    if os.path.exists('job_url.html'):
        os.remove('job_url.html')

    if os.path.exists('glassdoor_jobs.html'):
        os.remove('glassdoor_jobs.html')



glassdoor_jobs = glassdoor.glassdoor_api()
jobs = ziprecruiter.ziprecruiter_api()


for job in jobs['jobs']:
    site_name = "ziprecruiter"
    hiring_company = job['hiring_company']['name']
    get_time = job['posted_time_friendly']
    get_url = job['job_url'] 
    ziprecruiter_api = "ziprecruiter"
    with open('jobfilter.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([hiring_company, get_time, get_url,site_name])


cleanUp()
