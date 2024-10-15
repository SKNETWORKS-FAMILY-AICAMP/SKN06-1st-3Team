# SKN06-1st-3Team
<div align="center">

</div>

# 지역별 교통사고 데이터 조회 시스템 🚗
> **SK Networks AI CAMP 6기** <br/> **개발기간: 2024.10.11 ~ 2024.10.15 (총 5일)** <br/> **팀명: 몽몽크루🧸**

<br/>

<hr>

<br/>

### 개발팀 👩‍💻👨‍💻
| 성은진 | 박창규 | 공인용 | 김지영 |
|:----------:|:----------:|:----------:|:----------:|
| <img src="https://github.com/user-attachments/assets/711c6a05-31c3-43ba-b791-9b5c218144e3" alt="성은진" width="145" height="165" />  | <img src="https://github.com/user-attachments/assets/5c527f33-fa36-4c14-b6b3-a9594abe0425" alt="박창규" width="150" height="150" />  | <img src="https://github.com/user-attachments/assets/5179910a-50f5-4ec5-b23c-b90515c17cd1" alt="공인용" width="160" height="150" /> | <img src="https://github.com/user-attachments/assets/bab22e54-d0ba-4a1a-9e30-1fc6b497b651" alt="김지영" width="150" height="150" />|
| [@eunjinn05](https://github.com/eunjinn05) | [@Gumbeng](https://github.com/Gumbeng) | [@k348693](https://github.com/k348693) | [@yeong-ee](https://github.com/yeong-ee) |

<br/>

<hr>

<br/>

### 프로젝트 개요 🪄
해당 프로젝트는 시도 및 시군구별 도로 종류에 따른 교통사고 데이터를 조회하고, 자동차 기업의 FAQ를 함께 제공하는 시스템을 구축하는 것을 목표로 한다. 교통사고 데이터 분석을 통해 사용자는 특정 지역과 도로에서 발생하는 사고 통계를 조회할 수 있으며, 자동차 기업의 FAQ 조회 기능을 통해 차량 안전과 관련된 질문에 대한 답변을 쉽게 찾을 수 있다. 이 두 기능은 교통사고와 자동차 안전 정보를 통합하여 사용자에게 보다 종합적인 교통 안전 및 차량 관련 정보를 제공하는 데 중점을 둔다.

<br/>

<hr>

<br/>

### 기술 스택 ✨
<div>
        <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=MySQL&logoColor=white"/>
        <img src="https://img.shields.io/badge/Discord-5865F2?style=flat&logo=Discord&logoColor=white">
        <img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white">
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white"/>
</div>

<br/>

<hr>

<br/>

### 기능 소개 📱
1) 시도, 시군구별 도로 종류에 따른 교통사고 데이터 조회 시스템 제공
   - 전체 조회: 시도, 시군구, 사고 유형, 도로 종류 등
   - 그래프 조회
3) 자동차 제조사 정보 배경 FAQ 조회 시스템 제공
   - 전체 조회
   - 카테고리 검색: MY GENESIS 앱, 무선 소프트웨어 업데이트(OTA), 빌트인 캠, 정비예약, 제네시스 커넥티드 서비스, 차량 구매 등
   - 제목 검색
   - 내용으로 검색

<br/>

<hr>

<br/>

### ERD 🐾

<img src="https://github.com/user-attachments/assets/a4f1c1ad-8851-4a03-9926-f3b0a843747c" alt="ERD" width="600" height="400" />

<br/>

<hr>

<br/>

### 디렉토리 구조 ✍️

<br/>

<div style="width=500px">
```
bash
C:.
│  .DS_Store
│  .gitignore
│  accdent_sido.sql
│  accident.csv
│  accident__.csv
│  accident테이블.sql
│  app.py
│  config.ini
│  db accident_table category.sql
│  faq_data.py
│  graph.png
│  LICENSE
│  README.md
│  requirements.txt
│  시군구.sql
│
├─.ipynb_checkpoints
│      app-checkpoint.py
│      config-checkpoint.ini
│
├─accident
│  │  accident.ipynb
│  │  accident_class.py
│  │  untitled.txt
│  │
│  ├─.ipynb_checkpoints
│  │      accident-checkpoint.ipynb
│  │      accident_class-checkpoint.py
│  │      untitled-checkpoint.txt
│  │
│  └─__pycache__
│          accident_class.cpython-312.pyc
│
├─FAQ
│  │  crawling.py
│  │  faq_class.py
│  │  genesis_faq.py
│  │  hyundai_crawl.py
│  │  kia.py
│  │  requirements.txt
│  │  test.ipynb
│  │
│  ├─.ipynb_checkpoints
│  │      crawling-checkpoint.py
│  │      faq_class-checkpoint.py
│  │      hyundai_crawl-checkpoint.py
│  │      kia-checkpoint.py
│  │      requirements-checkpoint.txt
│  │
│  └─__pycache__
│          crawling.cpython-312.pyc
│          faq_class.cpython-312.pyc
│          hyundai_crawl.cpython-312.pyc
│          kia.cpython-312.pyc
│
├─faq_pagina
│  │  car_page.py
│  │  faq_pagination.py
│  │
│  ├─.ipynb_checkpoints
│  │      faq_pagination-checkpoint.py
│  │
│  └─__pycache__
│          car_page.cpython-312.pyc
│          faq_pagination.cpython-312.pyc
│
└─hyundai_faq
        answer.csv
        category.csv
        crawl.py
        hyundai_FAQ_ca_an.ipynb
        question.csv
```
        
</div>


<br/>

<hr>

<br/>

### 프로젝트 결과 (최종 Streamlit UI) ☄️
- 메인 페이지
<img src="https://github.com/user-attachments/assets/039b742f-b2a8-4352-9f75-aaf845f1a99b" alt="메인" width="600" height="320" />

<br/>

- 교통사고 데이터 조회 페이지
<img src= "https://github.com/user-attachments/assets/a3c72ea6-79fd-49fa-9a22-337099c6d416" alt="데이터조회" width="600" height="320" />

<br/>

- 교통사고 데이터 조회 > 전체 조회 페이지
<img src= "https://github.com/user-attachments/assets/3bb3b022-4db3-4693-a720-a2d2b46aa913" alt="데이터전체조회" width="600" height="320" />

<br/>

- 교통사고 데이터 조회 > 그래프 조회 페이지
<img src= "https://github.com/user-attachments/assets/93084bf0-9bd3-4b89-82d7-5b437b9dacc8" alt="데이터그래프조회" width="600" height="320" />

<br/>

- 자동차 관련 FAQ 조회 페이지
<img src= "https://github.com/user-attachments/assets/9f449d8e-18a2-4161-b59a-22af5c4cbfe7" alt="FAQ조회" width="600" height="320" />

- 자동차 관련 FAQ 조회 > 전체 조회 페이지
<img src= "https://github.com/user-attachments/assets/1465eb18-a95f-43a5-94ff-6a01e0b5baff" alt="FAQ전체조회" width="600" height="320" />

- 자동차 관련 FAQ 조회 > 카테고리별 조회 페이지
<img src= "https://github.com/user-attachments/assets/a7cfd67d-918a-47b5-97b0-8ce4edeae540" alt="FAQ카테고리검색" width="600" height="320" />
