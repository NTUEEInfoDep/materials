import requests
from bs4 import BeautifulSoup
import urllib

def chinese2url(chinese_query):
    return urllib.parse.quote(chinese_query.encode('big5'))

csname = '電子學'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15'

headers = {
    'User-Agent': user_agent,
}

data = {
    'MIME Type': 'application/x-www-form-urlencoded',
    'current_sem': '108-1',
    'cstype': 1,
    'csname': csname.encode('big5'), # 電子學
    'alltime': 'yes',
    'allproced': 'yes',
    'allsel': 'yes',
    'page_cnt': 1000,
    'Submit22': '查詢'.encode('big5') # 查詢
}

url = 'http://nol.ntu.edu.tw/nol/coursesearch/search_result.php'
res = requests.post(url, data = data, verify = False)
res.encoding = 'big5'
soup = BeautifulSoup(res.text, 'html.parser')
course_rows = soup.findAll('tr')
for course in course_rows:
    tds = course.findAll('td')
    if len(tds) != 18:
        continue
    course_id_1 = tds[0].text
    course_dept = tds[1].text
    course_id_2 = tds[2].text
    if tds[4].find('a') == None:
        continue
    course_name = tds[4].find('a').text