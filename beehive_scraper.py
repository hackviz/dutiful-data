import json
import bs4
from bs4 import BeautifulSoup

import urllib.request
import time

def parse_single_release(s):
    time.sleep(5)
    release = {}
    content = str(s.find_all('div', class_="content"))
    release['content'] = content.replace('<p>', '').replace('<p>', '').replace('</p>', '').replace('\n', '').replace('\\u', '')
    release['date'] = str(s.find('p', class_="date").contents[0].contents[0])
    release['portfolios'] = [str(a.contents) for a in s.find_all("a") if '/portfolio/' in str(a)]
    release['title'] = str(s.find_all('title')[0].contents[0][18:])
    release['minister'] = [str(a.contents) for a in s.find_all("a") if '/minister/' in str(a)]
    return release

if __name__ == '__main__':
    for i in range(277): 
        base = 'https://www.beehive.govt.nz'
        data = requests.get(base + '/releases?page={}'.format(i))
        soup = BeautifulSoup(data)
        paths = [s['href'] for s in soup.find_all('a') if '/release/' in s['href']]
        paths = [base+p for i, p in enumerate(paths) if i%2==0]

        releases = [BeautifulSoup(urllib.request.urlopen(p)) for p in paths]
        if len(releases) == 0:
            print(soup)
            raise SystemExit

        parsed_releases = [parse_single_release(s) for s in releases]
        for rel in parsed_releases:
            print('writing {}'.format(rel['title']))
            with open(rel['title'].replace(' ','').replace('$', '') + '.json', 'w') as f:
                json.dump(rel, f)	
