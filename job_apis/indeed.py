import requests
import pprint

cookies = {

}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.indeed.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Connection': 'keep-alive',
}
# https://www.indeed.com/jobs?q=Lab%20Assistant&l=Katy%2C%20TX&vjk=4d89c2165ee972d7&advn=2337189061980106

params = {
    'q': 'Lab Assistant',
    'l': 'Katy, TX',
  


}

response = requests.get('https://www.indeed.com/jobs', headers=headers, params=params, cookies=cookies)
for content in response.content.decode('utf-8').split('\n'):
    # pprint.pprint(content)
    
    if 'jobmap[' in content:
        _company = content.split('srcname:')[1].split(',')[0]
        _total_jumps = content.split('jobmap[')[1].split(']')[0]
        
        print(_company,_total_jumps)
        # break

# with open('indeed.html', 'wb') as f:
#     f.write(response.content)



# with open("indeed.html") as fp:
#     for line in fp:
#         if 'jobmap[' in line:
#             job_srcname = line.split('srcname:')[1].split(',')[0]
#             print(job_srcname)




