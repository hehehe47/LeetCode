import requests

header = {
    # ':authority':'www.vitals.com',
    # ':method':'GET',
    # ':path':'/search/ajax?city_state=Washington,%20DC&latLng=38.892091,-77.024055&page=1&reqNo=0',
    # ':scheme':'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d8c9dc95c3d49bb4d422c260cd094fb221573007724; PHPSESSID=9u570g1l41imkgsaqcfc4d6scq; rmid=1rmp7k; rspec=podt; rfspec=pods-pods; rpspec=podt; rspex=4419%7C5122; retarget=%7B%22spec%22%3A%5B%22podt%22%5D%2C%22mid%22%3A%5B%221rmp7k%22%5D%2C%22pspec%22%3A%5B%22podt%22%5D%2C%22fspec%22%3A%5B%22pods-pods%22%5D%7D; _ga=GA1.2.280930436.1573007726; _gid=GA1.2.526023078.1573007726; s_fid=353C0BCF9084731D-1427996B9D8055EA; s_cc=true; _fbp=fb.1.1573007727095.720010039; app-c[reviewIntercept]=1573007733643; __qca=P0-1243920216-1573007761877; __gads=ID=6cb773e7e5737c8e:T=1573007762:S=ALNI_MZeHFFODApx-cje95mCEOgdnipo5A; lpid=cb33b33e5e5fee83b6a999f6ddc2d29d; ads_sess={%22pim%22:{%22c%22:%22pimc_1x%22%2C%22t%22:%22pimt_1573007934163x%22}}; mnet_session_depth=7%7C1573007931037; s_sq=%5B%5BB%5D%5D; __cfruid=0a44554be11d446082e1e475a656af1f7e8080f8-1573066383; _dc_gtm_UA-2543312-1=1',
    'referer': 'https://www.vitals.com/search?city_state=Washington,%20DC&latLng=38.892091,-77.024055&page=1',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'}
from bs4 import BeautifulSoup as bs

b = requests.get('https://www.vitals.com/search?city_state=Washington,%20DC&latLng=38.892091,-77.024055&page=1',
                 headers=header)
print(b.text)
s = bs(b.text)
# a = s.select('div[id="select_company"] > ul[class="xl2"] > li > label') #soup.select('div > span')
# l = []
# for i in a:
#     j = i.text
#     j = j.lower()
#     l.append(j.strip())
# print(len(l))
# tmp = ['Facebook','Apple','amazon','Google','pinterest','Goldman','Cisco','SAP','Akuna','VMware','Amex','Robinhood','Nvidia','Salesforce(quip)','Citadel','Jane Street','Yelp','Samsara','Square','Twitter','Visa','lime','IXL learning','Palantir','Databricks','EA','Qualcomm','IBM','Affinity','Qualtrics','Duolingo','Citrix','Viasat','DropBox','MathWorks','factual','Flexport','Dell','Prosper','Lucid Motors','SAP','Thumbtack','godaddy','blackrock','wish','stripe','intuit','Gusto','DiDi ','Egnyte','HubSpot','aurora','Aruba (HPE)','LiveRamp','applied intuition','PayPal','Bolt','viagogo','vArmour','Affirm','Evidation','Wayfair','clutter','Conversant','c3.ai','ripple','brex','Lyft','DataVisor','SeatGeek','Splunk','convoy','Bloomberg','Redfin','memSQL','Rubrik','Impira','Anomali','Ike','Cockroach Labs','Celo','VISA','rti','Asana','ubs','Airbnb','Confluent','Quantcast','Twilio','Uber','Plaid','leetcode ','Optiver','peak6','automation anywhere','pure storage','Squarespace','MongoDB','Tripadvisor','Whisper.ai','Quora','nuro','Oracle','Linkedin','Adobe','Microsoft','boa','citi','Obsidian','HeadSpin','Embark Trucks','FactSet','expedia','docusign','twosigma','Intel']
# tmp = [k.lower() for k in tmp]
# print(len(tmp))
# count=0
# for i in l:
#     if i not in tmp:
#         print(i)
#         count+=1
# print(count)

# print(a)
# print(type(a))
