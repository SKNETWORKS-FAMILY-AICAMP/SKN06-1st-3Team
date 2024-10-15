import json
import requests  # requests 라이브러리 임포트
from bs4 import BeautifulSoup
from pprint import pprint

def kias():
    base_url = 'https://www.kia.com/content/cq:graphql/global/endpoint.json'
    
    # category, keyword, locale 인자들을 제거한 쿼리
    params = {
        "operationName": "faqList",
        "variables": {},
        "query": """
        query faqList {
            faqList {
                items {
                    _path
                    question
                    answer {
                        html
                        plaintext
    
                    }
                    tags
                }
            }
        }
        """
    }
    
    req_headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    
    res = requests.post(base_url, json=params, headers=req_headers)
    
    if res.status_code == 200:
        try:
            # 응답 텍스트 확인
            
            text = json.loads(res.text)
            tmp =[]
            cnt = 0
            temp = {"etc":"기타","pbv":"PBV","homepage":"홈페이지","buy":"차량구매","repair":"차량정비","kia-members":"기아멤버스"}
            for i in range(len(text['data']['faqList']['items'])):
                title = text['data']['faqList']['items'][i]['question']
                content = text['data']['faqList']['items'][i]['answer']['plaintext']
                paths = text['data']['faqList']['items'][i]['_path'].replace("/content/dam/kwp/kr/ko/data/faq/", "")
                paths = paths.split("/")[0]
                if paths not in temp:
                    paths = "기타"
                else:
                    paths = temp.get(paths)
                tmp.append([paths, title, content])
            return tmp
        except json.JSONDecodeError as e:
            return None
    
    else:
        return None