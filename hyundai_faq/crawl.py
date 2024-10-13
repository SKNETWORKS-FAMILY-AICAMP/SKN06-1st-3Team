from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def next_category():
    try : 
        ctgr_next = driver.find_element(By.XPATH, f'//*[@id="app"]/div[3]/section/div[2]/div/div[2]/section/div/div[1]/div[1]/ul/li[{b}]/button')
        time.sleep(0.1)
        ctgr_next.click()
        time.sleep(0.3)
    except ElementClickInterceptedException as e :
        return e
    return

def get_category():
    category_elements = driver.find_elements(By.XPATH, '//button[@title="콘텐츠 확장됨"]/div/span[1]')
    ctgr = [ca.text.strip() for ca in category_elements]
    for c in ctgr:
        category1.append(c)
    time.sleep(0.1)
    return

def get_answer():
    answer_elements = driver.find_elements(By.XPATH, '//button[@title="콘텐츠 확장됨"]/following-sibling::div[1]/div')
    ans = [an.text for an in answer_elements]
    for a in ans:
        answer1.append(a)
    time.sleep(0.1)
    return

def get_question():
    question_elements = driver.find_elements(By.CSS_SELECTOR, "span.list-content")
    qstn = [element.text.strip() for element in question_elements]
    for q in qstn:
        question1.append(q)
    time.sleep(0.1)
    return

def next_page():
    try:
        next = driver.find_element(By.XPATH, "//li[contains(@class,'number active')]/following-sibling::li[1]/button")
        time.sleep(0.1)
        next.click()
        time.sleep(0.5)
        return
    except Exception as e:
        return e
def prev_all_page():
    prev = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-prevall")
    time.sleep(0.1)
    prev.click()
    time.sleep(0.5)
    return
#----------------------------------------------------------------------------------------------------

for b in range(2,10):   # 다음 카테고리 반복
    try:
        try:
            for q in range(20):
                get_question()
                extend_buttons = driver.find_elements(By.XPATH, "//button[@class=\"list-title\"]")
                for ext in extend_buttons:   # 페이지 내의 질문 확장 버튼 반복
                    time.sleep(0.1)
                    ext.click()
                    time.sleep(0.3)
                    get_category()
                    get_answer()             # 클릭해야 보여지고 다음항목 클릭 시 사라짐
                    time.sleep(0.1)
                next_page()
        except:                              # 페이지 수가 항목마다, 브라우저 크기마다 달라서 다음 페이지 없을 때 넘어가도록 함
            print("마지막페이지")
            prev_all_page()                  # 마지막 페이지에서 다음 카테고리 이동 시 페이지 버그 발생.
        next_category()                      # 첫 페이지로 맞춘 후 카테고리 이동
    except:
        print("페이지 크롤링완료")            # 
        