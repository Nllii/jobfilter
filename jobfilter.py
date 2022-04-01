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
        for number, joblist in enumerate(csv_reader, start=0):
            webbrowser.open(joblist[2])
            time.sleep(1)
            input("Press Enter to continue...")
            # close the previous webbrowser tab 
            # webbrowser.open_new_tab('about:blank')

            with open('jobs_applied.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([joblist[0], joblist[1], joblist[2], joblist[3]])
            if number == 0:
                print(f"{count} jobs have been applied to")
            else:
                count += 1
                print(f"{joblist[0]}")
                print(f"{joblist[1]}")
                print(f"{joblist[2]}")
                print(f"{count} jobs have been applied to")
                print("\n")


        

# # remove the old csv_file

def removeOldCsv():
    if os.path.exists('jobfilter.csv'):
        os.remove('jobfilter.csv')
    
    # if os.path.exists('jobs_applied.csv'):
    #     os.remove('jobs_applied.csv')


    with open('jobfilter.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['hiring_company', 'get_time', 'get_url', 'site_name'])


def cleanUp():
    if os.path.exists('job_url.html'):
        os.remove('job_url.html')

    if os.path.exists('glassdoor_jobs.html'):
        os.remove('glassdoor_jobs.html')
        

def start_Job_Search():
    glassdoor.glassdoor_api(keyword= 'lab assistant')
    ziprecruiter.ziprecruiter_api(search='lab assistant',radius = 10,city= "Houston",state_abbrev="TX")




removeOldCsv()
start_Job_Search()
cleanUp()
read_csv()


