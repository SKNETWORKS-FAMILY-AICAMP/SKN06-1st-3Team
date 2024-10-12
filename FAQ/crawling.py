import requests
from bs4 import BeautifulSoup
import configparser
# 크롤링
# Config 파일 읽기
config = configparser.ConfigParser()
config.read('config.ini')  # config.ini 파일을 읽음

# Config에서 크롤링 설정값 가져오기
url = config['CRAWLING']['url']
user_agent = config['CRAWLING']['user_agent']

def crawl_data():
    # 요청 헤더 설정
    headers = {"user-agent": user_agent}
    
    # HTTP GET 요청 보내기
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "lxml")
        faq_list = soup.select("a.accordion-btn")
        # 추출한 데이터 넣어줄 배열
        search_names = []
    
        for txt in faq_list:
            # 태그 내의 텍스트 추출 후 공백 제거
            title = txt.select_one("p.accordion-title").get_text(strip=True)
            category = txt.select_one("strong.accordion-label").get_text(strip=True)
    
            # div 태그 내의 p 테그 텍스트 추출
            div = txt.find_next("div", class_="accordion-panel")
            panel_texts = [p.get_text(strip=True) for p in div.select("p")]
    
            content = ''
            for contxt in panel_texts:
                content += contxt + '\n'
            search_names.append([category, title, content])

        return search_names

    else:
        return None