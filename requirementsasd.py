from bs4 import BeautifulSoup
import re
import json
from subprocess import check_output
import requests
import time
from tqdm import tqdm #tqdm is just to implement a progress bar, https://pypi.org/project/tqdm/

cars = [] #create empty list to which we will append the car dicts from the json data

url = 'https://www.cardekho.com/used-cars+in+bangalore'
r = requests.get(url , headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content.decode('utf-8'),"html.parser")
s = soup.find('script', {"type":"application/ld+json"}).next_sibling #find the section with the json data. It looks for a script tage with application/ld+json type, and takes the next tag, which is the one with the data we need, see page source code

js = 'window = {};n'+s.text.strip()+';nprocess.stdout.write(JSON.stringify(window.__INITIAL_STATE__));' #strip the text from unnecessary strings and load the json as python dict, taken from: https://stackoverflow.com/questions/54991571/extract-json-from-html-script-tag-with-beautifulsoup-in-python/54992015#54992015
with open('temp.js','w') as f: # save the sting to a javascript file
    f.write(js)

data_site = json.loads(check_output(['node','temp.js'])) #execute the file with node, which will return the json data that will be loaded with json.loads.
for i in data_site['items']: #iterate over the dict and append all cars to the empty list 'cars'
  cars.append(i)

for page in tqdm(range(20, data_site['total_count'], 20)): #'pagefrom' in the api call is 20, 40, 60, etc. so create a range and loop it
  r = requests.get(f"https://www.cardekho.com/api/v1/usedcar/search?&cityId=105&connectoid=&lang_code=en&regionId=0&searchstring=used-cars%2Bin%2Bbangalore&pagefrom={page}&sortby=updated_date&sortorder=asc&mink=0&maxk=200000&dealer_id=&regCityNames=&regStateNames=", headers={'User-Agent': 'Mozilla/5.0'})
  data = r.json()

  for i in data['data']['cars']: #iterate over the dict and append all cars to the empty list 'cars'
    cars.append(i)

  time.sleep(5) #wait a few seconds to avoid overloading the site

