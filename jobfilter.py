from job_apis import ziprecruiter
import pprint
import csv


jobs = ziprecruiter.ziprecruiter_api()


for job in jobs['jobs']:
    # pprint.pprint(job)
    hiring_company = job['hiring_company']['name']
    get_time = job['posted_time_friendly']
    get_url = job['job_url'] 
    # save to csv file 
    with open('jobfilter.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([hiring_company, get_time, get_url])



