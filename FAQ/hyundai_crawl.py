from bs4 import BeautifulSoup
import json
import requests
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def hyundai_crawl():    
    category_code = ['01','02','03','04','06','07','08','09','10']
    size = ['36','40','32','11','76','29','17','7','1']
    
    base_url = 'https://www.hyundai.com/kr/ko/gw/customer-support/v1/customer-support/faq/list'
    url = base_url.format("post")
    
    question_list = []
    answer_list = []
    category_list = []
    for x in range(9):
        params = {
            "siteTypeCode":"H",
            "faqCategoryCode":f"{category_code[x]}",
            "faqCode":"",
            "faqSeq":"",
            "searchKeyword":"",
            "pageNo":1,
            "pageSize":f"{size[x]}",
            "externalYn":""
        }
        
        req_headers = {
            'authority': 'www.hyundai.com',
            'method' : 'POST',
            'path' : '/kr/ko/gw/customer-support/v1/customer-support/faq/list',
            'scheme' : 'https',
            'accept' : 'application/json, text/plain, */*',
            'accept-encoding' : 'gzip, deflate, br, zstd',
            'accept-language' :'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length' : '128',
            'content-type':'application/json;charset=UTF-8',
            'cookie':'renderid=rend01; SCOUTER=x3fne0335t6om1; s_tp=3108; AMCVS_F46554D957710F697F000101%40AdobeOrg=1; s_ecid=MCMID%7C65914177975992605290850530518624212213; s_cc=true; s_dslv=1728543275431; s_tslv=1728543275432; s_ips=1844; s_ppv=company%253Air%253Air-resources%253Asales-results%2C87%2C59%2C2708%2C3%2C3; _gcl_au=1.1.478503182.1728546490; _fbp=fb.1.1728546489757.937871210524224114; _hjSessionUser_3642388=eyJpZCI6IjA0Y2NlNmQzLTkyNmEtNWZhMy05NGRhLTgzOTYxYjI2Mzg2ZSIsImNyZWF0ZWQiOjE3Mjg1NDY0ODk4NjMsImV4aXN0aW5nIjp0cnVlfQ==; AMCV_F46554D957710F697F000101%40AdobeOrg=179643557%7CMCIDTS%7C20011%7CMCMID%7C65914177975992605290850530518624212213%7CMCAAMLH-1729469478%7C11%7CMCAAMB-1729469478%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1728871878s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; _gid=GA1.2.7993254.1728864679; _hjSession_3642388=eyJpZCI6IjAyMmFlNTdlLWY5NTktNDNlZS1hYjc5LWExZDM5YTAxODAxYiIsImMiOjE3Mjg4NjQ2NzkxNzUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga=GA1.2.687742055.1728543272; gpv_pn=menu-list; s_sq=hm-kr-prd%3D%2526c.%2526a.%2526activitymap.%2526page%253Dmenu-list%2526link%253DFAQ%252520%252528%2525EC%25259E%252590%2525EC%2525A3%2525BC%2525ED%252595%252598%2525EB%25258A%252594%252520%2525EC%2525A7%252588%2525EB%2525AC%2525B8%252529%2526region%253DcustomerService%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dmenu-list%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.hyundai.com%25252Fkr%25252Fko%25252Fe%25252Fcustomer%25252Fcenter%25252Ffaq%2526ot%253DA%26hmworldwide%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcompany%25253Air%25253Air-resources%25253Asales-results%2526link%253D2024%2525EB%252585%252584%252520%2525EC%2525B0%2525A8%2525EC%2525A2%252585%2525EB%2525B3%252584%252520%2525EB%2525A7%2525A4%2525EC%2525B6%25259C%2525EC%25258B%2525A4%2525EC%2525A0%252581%2525ED%25258C%25258C%2525EC%25259D%2525BC%252520%2525EB%25258B%2525A4%2525EC%25259A%2525B4%2525EB%2525A1%25259C%2525EB%252593%25259C%2526region%253DsalesPerformanceData%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcompany%25253Air%25253Air-resources%25253Asales-results%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BfileDownload%252528%252527%25252Fcontent%25252Fdam%25252Fhyundai%25252Fww%25252Fen%25252Fimages%25252Fcompany%25252Finvestor-relations%25252Fir%2526oidt%253D2%2526ot%253DBUTTON; _ga_3T0QQVQ54K=GS1.1.1728867144.4.1.1728867167.37.0.0; _gat_gtag_UA_46360746_1=1',
            'ep-channel':'homepage',
            'ep-ip':'127.0.0.1',
            'ep-jsessionid':'',
            'ep-menu-id': '',
            'origin':'https://www.hyundai.com',
            'priority':'u=1, i',
            'referer':'https://www.hyundai.com/kr/ko/e/customer/center/faq',
            'sec-ch-ua':'"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':"macOS",
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-b3-sampled':'1',
        }
        
        res = requests.post(
            url,
            json=params,
            headers=req_headers
        )
    
        if res.status_code == 200:
            text = json.loads(res.text)
            cnt = text['data']['total']
            for i in range(0, cnt) :
                question_list.append(text['data']['list'][i]['faqQuestion'])
                # cleantext = cleanhtml(text['data']['list'][i]['faqAnswer'])
                # answer_list.append(cleantext)
    
                clean_text = BeautifulSoup(text['data']['list'][i]['faqAnswer'], "lxml").get_text(strip=True)
                answer_list.append(clean_text)
                # answer_list.append(text['data']['list'][i]['faqAnswer'])                    ##### 태그제거 필요
                
                category_list.append(text['data']['list'][i]['faqCategoryName'])
        else:
            print("실패:", res.status_code)
    answer_list2 = [cleanhtml(txt) for txt in answer_list]
    answer_list3 = [cleanhtml(txt) for txt in answer_list2]    #### 태그 제거
    FAQ_list =[]
    for i in range(len(category_list)):
        faq = [category_list[i], question_list[i], answer_list3[i]]
        # print(faq)
        FAQ_list.append(faq)

    return FAQ_list

