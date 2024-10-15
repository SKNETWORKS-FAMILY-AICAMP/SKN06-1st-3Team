# app.py

import streamlit as st
from faq_pagina.faq_pagination import display_faq_section, get_dao # faq_handler.py에서 FAQ 관련 함수 불러오기
from faq_pagina.car_page import display_accident, car_dao

# DAO 객체 생성
dao = get_dao()
car_dao = car_dao()

# Streamlit 페이지 설정
st.set_page_config(page_title="FAQ 페이지", layout="wide")

# 사이드바에서 'FAQ'와 'DATA' 중 선택
by = st.sidebar.radio("목록", ["FAQ", "DATA"])

# FAQ 선택 시 faq_handler.py에서 정의된 display_faq_section 함수 호출
if by == "FAQ":
    display_faq_section(dao)
    
elif by == "DATA" :
    display_accident(car_dao)