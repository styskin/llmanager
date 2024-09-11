from bs4 import BeautifulSoup
import urllib.request
import ssl
import sys
import time

ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://peregovorshiki.ru/kejsy/ekspress-situatsii.html?start=%d&layout=shaper_educonblognoticeboard"

def get_page(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


with open('express.txt', 'a') as f:
    for i in range(0, int(558 / 15) + 1):
        text = get_page(URL % (i))
        soup = BeautifulSoup(text)
        
        for s in soup.find_all('div', 'entry-header'):
            m = s.find_all("p")
            d = dict()
            d["situation"] = m[0].contents[0]
            d["question"] = m[1].find("strong").contents[0]
            f.write(str(d) + '\n')
        #time.sleep(1)
        if i % 10 == 0:
            print("%d" % i, file=sys.stderr)