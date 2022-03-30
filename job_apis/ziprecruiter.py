import requests
import pprint
import csv


def ziprecruiter_api():
    
    headers = {
    'User-Agent': 'Job Search/3084 (iPhone; CPU iOS 14_0 like Mac OS X)',
    'Authorization': 'Basic YTBlZjMyZDYtN2I0Yy00MWVkLWEyODMtYTI1NDAzMzI0YTcyOg==',
}

    params = {
        'allow_currency': 'USD',
        'days': '2',
        'location': 'Houston, TX',
        'radius': '30',
        'search': 'Lab assistant',
    }

    response = requests.get('https://api.ziprecruiter.com/jobs-app/jobs', headers=headers, params=params)
    data = response.json()
    # return data
    for job in data['jobs']:
        site_name = "ziprecruiter"
        hiring_company = job['hiring_company']['name']
        get_time = job['posted_time_friendly']
        get_url = job['job_url'] 
        with open('jobfilter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([hiring_company, get_time, get_url,site_name])
