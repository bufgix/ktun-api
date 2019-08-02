from dataclasses import dataclass
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re


@dataclass
class Links:
    announcements_base_link = "http://ktun.edu.tr/Home/TumDuyurular"

def get_announcements():
    req = requests.get(Links.announcements_base_link)
    soup = BeautifulSoup(req.text, 'html.parser')
    rows = soup.find('tbody').find_all('tr')
    
    content = []
    for row in rows:
        contents = row.find_all('td')
        match = re.match('/Home/Duyuru/(\d+)', contents[3].find('a')['href'])
        if match:
            id = match.group(1)
        else:
            id = None
        content.append({
            'id': id,
            'title': contents[0].string,
            'started_date': datetime.strptime(contents[1].string, '%d.%m.%Y'),
            'end_date': datetime.strptime(contents[2].string, '%d.%m.%Y')
        })
    return content

if __name__ == "__main__":
    __import__('pprint').pprint(get_announcements())
