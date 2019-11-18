import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

res = requests.get('https://web.ee.ntu.edu.tw/teacher_index3.php')
soup = BeautifulSoup(res.text, 'html.parser')

teachers = soup.findAll("div", {"class": "teacher_list_intro"})
for div in teachers:
    name = div.find('td', {"class": "teacher_list_title"}).find('a').text
    email = parse_qs(urlparse(div.find('img')['src']).query)['email'][0]
    print("{} : {}".format(name.ljust(50), email))
