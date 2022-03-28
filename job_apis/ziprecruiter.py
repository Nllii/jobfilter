import requests
import pprint


def ziprecruiter_api():
    
    headers = {
    'User-Agent': 'Job Search/3084 (iPhone; CPU iOS 14_0 like Mac OS X)',
    'Authorization': 'Basic YTBlZjMyZDYtN2I0Yy00MWVkLWEyODMtYTI1NDAzMzI0YTcyOg==',
}

    params = {
        'allow_currency': 'USD',
        'days': '5',
        'location': 'Houston, TX',
        'radius': '30',
        'search': 'Lab assistant',
    }

    response = requests.get('https://api.ziprecruiter.com/jobs-app/jobs', headers=headers, params=params)
    data = response.json()
    return data
