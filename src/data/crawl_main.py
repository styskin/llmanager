from bs4 import BeautifulSoup
import urllib.request
import ssl
import sys
import time

ssl._create_default_https_context = ssl._create_unverified_context

HOST = "https://peregovorshiki.ru"
URL = "/kejsy/situatsii.html?layout=shaper_educonblognoticeboard&start=%d"
STEP = 25
TOTAL = 694

def get_page(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


with open('main.txt', 'a') as f:
    for i in range(0, int(TOTAL / STEP) + 1):
        text = get_page((HOST + URL) % (i))
        soup = BeautifulSoup(text)
        
        for s in soup.find_all('a', 'btn-primary'):
            case_doc = BeautifulSoup(get_page(HOST + s['href']))
            situation = case_doc.find('div', attrs={'itemprop':'articleBody'})
            # print(situation.get_text().strip())
            d = dict()
            d["situation"] = situation.get_text().strip()
            f.write(str(d) + '\n')
        #time.sleep(1)
        if i % 10 == 0:
            print("%d" % i, file=sys.stderr)