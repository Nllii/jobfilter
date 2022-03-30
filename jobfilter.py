from job_apis import ziprecruiter
from job_apis import glassdoor
import webbrowser
import csv
import os
import time

# open and read csv file to get job urls
count=0 
def read_csv():
    global count
    with open('jobfilter.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for number, joblist in enumerate(csv_reader, start=1):
            webbrowser.open(joblist[2])
            time.sleep(5)
            if number % 3 == 0:
                input("Press Enter to continue...")


        

# # remove the old csv_file

def removeOldCsv():
    if os.path.exists('jobfilter.csv'):
        os.remove('jobfilter.csv')

    with open('jobfilter.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['hiring_company', 'get_time', 'get_url', 'site_name'])


def cleanUp():
    if os.path.exists('job_url.html'):
        os.remove('job_url.html')

    if os.path.exists('glassdoor_jobs.html'):
        os.remove('glassdoor_jobs.html')

def start_Job_Search():
    glassdoor.glassdoor_api()
    ziprecruiter.ziprecruiter_api()




removeOldCsv()
start_Job_Search()
cleanUp()
read_csv()


