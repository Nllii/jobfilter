import requests
import pprint

cookies = {

    'CO': 'US',
    'LOCALE': 'en',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.indeed.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Referer': 'https://www.indeed.com/?from=mobRdr',
    'Connection': 'keep-alive',
}

params = {
    'q': 'Lab Assistant',
    'l': 'Katy, TX',
    'start': '0',
    'limit': '100',
    'radius': '25',

}

response = requests.get('https://www.indeed.com/jobs', headers=headers, params=params, cookies=cookies)
for content in response.content.decode('utf-8').split('\n'):
    # pprint.pprint(content)
    
    if 'jobmap[' in content:
        _company = content.split('srcname:')[1].split(',')[0]
        print(_company)
        # break

# with open('indeed.html', 'wb') as f:
#     f.write(response.content)



# with open("indeed.html") as fp:
#     for line in fp:
#         if 'jobmap[' in line:
#             job_num = line.split('jobmap[')[1].split(']')[0]
#             job_srcname = line.split('srcname:')[1].split(',')[0]
#             print(job_srcname)




