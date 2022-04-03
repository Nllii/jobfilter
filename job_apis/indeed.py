import requests
import bs4
import re
import json

cookies = {
    'PTK': 'tk=1fvn4b0ges7ij800&type=jobsearch&subtype=topsearch',
    'CSRF': 'iwNLtqSz5fJMs0bXHhglzy7JqYcwlJYY',
    'PPID': 'eyJraWQiOiJhOTU2Yzg2NC1mNGNkLTQzYzMtYTVjYy00NDQ4ZWRlMDJmM2UiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI3NjdmYjZlY2NmMWQ4YzY2IiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF1dGgiOiJhcHBsZSIsImNyZWF0ZWQiOjE2NDc5Mzc1NzYwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjQ4OTcxODEyLCJpYXQiOjE2NDg5NzAwMTIsImxvZ190cyI6MTY0ODk2Nzk1MjQ2NiwiZW1haWwiOiJyZjR3Y216OGc2QHByaXZhdGVyZWxheS5hcHBsZWlkLmNvbSJ9.o3ubyA6NkJd5BaUF7ywKgDwnPl-PD4xQ45ZYtZOeYFg1eq0BLz5gNPGjMUecMoufDcmxt36MEPS5XgEl6jE7_A',
    'LV': '"LA=1648969831:CV=1648968971:TS=1643806307"',
    'indeed_rcc': '"LOCALE:PREF:LV:CTK:CO:UD:RQ"',
    'CTK': '1fqt7rd9ht5bt800',
    'LC': '"co=US"',
    'INDEED_CSRF_TOKEN': '1CO74qqX4k3IhdoE22Rp7tA3i7BEdORU',
    'ac': 'j1wKALMdEey4UwsIQ1J7eA#j1z0YLMdEey4UwsIQ1J7eA',
    'UD': '"LA=1648969831:CV=1648968971:TS=1643806307"',
    'NOMOB': '1',
    'MICRO_CONTENT_CSRF_TOKEN': 'tO04wbV2KcyTLWaPvgtD8T8ILUHwIbz6',
    'JSESSIONID': 'FCADFADD754194AF6966914D1ADA2373',
    'pjps': '1',
    'RQ': '"q=laboratory&l=Houston%2C+TX&ts=1648969831397:q=Test&l=Houston%2C+TX&ts=1648969385432"',
    'jaSerpCount': '5',
    'RCLK': 'jk=c621543f11b7206b&tk=1fvn3rcbft4u0802&from=web&rd=VwIPTVJ1cTn5AN7Q-tSqGRXGNe2wB2UYx73qSczFnGU&qd=RnZhMybXSk4M3QtTVGXWoWpikWSYD-BX7A_IE8OoskrZePQgM0kFyNjBeO3tyxqFa1xW5qBYyuSGq6vAN7OQ_SKDynEgwb20xtfEJDZmhbo1Vu4aS9dH_tvzuwb-B6Jr&ts=1648969494895&sal=1',
    'RSJC': '126c0cf170fa976e:c29cb54a548cdaad:1dedcd881b4800bf:4d89c2165ee972d7',
    'jobAlertPopoverShown': '1',
    'SHARED_INDEED_CSRF_TOKEN': '1CO74qqX4k3IhdoE22Rp7tA3i7BEdORU',
    'PREF': '"TM=1648968979151:L=Houston%2C+TX"',
    'CO': 'US',
    'LOCALE': 'en',
    'SURF': 'mYdqfiFdENvOZUL2I2Ltjb8E5FaPegkX',
    'SHOE': '"42tJe9lnloQt6bmU4JPWX_YxlIx5vO1aqkHGE_Tb55K9IYpKPFsxmlHmH-JIO0cNil5wsqat-JerXtrzabot8l4k7hRDXzcmfIpNtaSWAb9lx6BRyWghQXynXRCeRu3ctE3KDjFTqYdRKD_4sC9CLY_L9Q=="',
    'SOCK': '"qfD1C9ecdRkna8nC0EsLAxEf5yI="',
    '__ssid': 'ee00dd9c0facd0a2a8c40cccadf0815',
    'indeed_rcc': 'CTK',
    'cmppmeta': '"eNoBSAC3/+BkY3Tg/k3km7p5N390reKS0k4ChrqLik1HNpYJSQHfohMlTnQeYzieqtDxrc4WIX7XZPKFq0sSED4U6mA9Isi6f4Ul2dES4SVfIug="',
    'CMP_VISITED': '1',
    'CO': 'US',
    'LOCALE': 'en',
}

headers = {
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PTK=tk=1fvn4b0ges7ij800&type=jobsearch&subtype=topsearch; CSRF=iwNLtqSz5fJMs0bXHhglzy7JqYcwlJYY; PPID=eyJraWQiOiJhOTU2Yzg2NC1mNGNkLTQzYzMtYTVjYy00NDQ4ZWRlMDJmM2UiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiI3NjdmYjZlY2NmMWQ4YzY2IiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF1dGgiOiJhcHBsZSIsImNyZWF0ZWQiOjE2NDc5Mzc1NzYwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjQ4OTcxODEyLCJpYXQiOjE2NDg5NzAwMTIsImxvZ190cyI6MTY0ODk2Nzk1MjQ2NiwiZW1haWwiOiJyZjR3Y216OGc2QHByaXZhdGVyZWxheS5hcHBsZWlkLmNvbSJ9.o3ubyA6NkJd5BaUF7ywKgDwnPl-PD4xQ45ZYtZOeYFg1eq0BLz5gNPGjMUecMoufDcmxt36MEPS5XgEl6jE7_A; LV="LA=1648969831:CV=1648968971:TS=1643806307"; indeed_rcc="LOCALE:PREF:LV:CTK:CO:UD:RQ"; CTK=1fqt7rd9ht5bt800; LC="co=US"; INDEED_CSRF_TOKEN=1CO74qqX4k3IhdoE22Rp7tA3i7BEdORU; ac=j1wKALMdEey4UwsIQ1J7eA#j1z0YLMdEey4UwsIQ1J7eA; UD="LA=1648969831:CV=1648968971:TS=1643806307"; NOMOB=1; MICRO_CONTENT_CSRF_TOKEN=tO04wbV2KcyTLWaPvgtD8T8ILUHwIbz6; JSESSIONID=FCADFADD754194AF6966914D1ADA2373; pjps=1; RQ="q=laboratory&l=Houston%2C+TX&ts=1648969831397:q=Test&l=Houston%2C+TX&ts=1648969385432"; jaSerpCount=5; RCLK=jk=c621543f11b7206b&tk=1fvn3rcbft4u0802&from=web&rd=VwIPTVJ1cTn5AN7Q-tSqGRXGNe2wB2UYx73qSczFnGU&qd=RnZhMybXSk4M3QtTVGXWoWpikWSYD-BX7A_IE8OoskrZePQgM0kFyNjBeO3tyxqFa1xW5qBYyuSGq6vAN7OQ_SKDynEgwb20xtfEJDZmhbo1Vu4aS9dH_tvzuwb-B6Jr&ts=1648969494895&sal=1; RSJC=126c0cf170fa976e:c29cb54a548cdaad:1dedcd881b4800bf:4d89c2165ee972d7; jobAlertPopoverShown=1; SHARED_INDEED_CSRF_TOKEN=1CO74qqX4k3IhdoE22Rp7tA3i7BEdORU; PREF="TM=1648968979151:L=Houston%2C+TX"; CO=US; LOCALE=en; SURF=mYdqfiFdENvOZUL2I2Ltjb8E5FaPegkX; SHOE="42tJe9lnloQt6bmU4JPWX_YxlIx5vO1aqkHGE_Tb55K9IYpKPFsxmlHmH-JIO0cNil5wsqat-JerXtrzabot8l4k7hRDXzcmfIpNtaSWAb9lx6BRyWghQXynXRCeRu3ctE3KDjFTqYdRKD_4sC9CLY_L9Q=="; SOCK="qfD1C9ecdRkna8nC0EsLAxEf5yI="; __ssid=ee00dd9c0facd0a2a8c40cccadf0815; indeed_rcc=CTK; cmppmeta="eNoBSAC3/+BkY3Tg/k3km7p5N390reKS0k4ChrqLik1HNpYJSQHfohMlTnQeYzieqtDxrc4WIX7XZPKFq0sSED4U6mA9Isi6f4Ul2dES4SVfIug="; CMP_VISITED=1; CO=US; LOCALE=en',
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
    'l': 'Houston, TX',
}

response = requests.get('https://www.indeed.com/jobs', headers=headers, params=params, cookies=cookies)
for content in response.content.decode('utf-8').split('\n'):
    if 'jobmap[' in content:
        _company = content.split('srcname:')[1].split(',')[0]
        print(_company)
        break

# with open('indeed.html', 'wb') as f:
#     f.write(response.content)



# with open("indeed.html") as fp:
#     for line in fp:
#         if 'jobmap[' in line:
#             job_num = line.split('jobmap[')[1].split(']')[0]
#             job_srcname = line.split('srcname:')[1].split(',')[0]
#             print(job_srcname)




