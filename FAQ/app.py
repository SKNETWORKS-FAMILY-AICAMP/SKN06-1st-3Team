import streamlit as st
import faq_class as FAQDao
import configparser as parser

def get_dao():
    props = parser.ConfigParser() # parser 생성
    props.read("config.ini") # ini 파일 읽기
    config = props['MYSQL'] # section이름으로 읽기
    dao = FAQDao.FAQDao(host=config['host'], port=3306, user=config['user'], 
                        password=config['password'], db=config['db'])
    return dao

dao = get_dao()

st.set_page_config(page_title="SK06_01_3Tim")


by = st.sidebar.radio("목록", ["FAQ","DATA"])

if by == "FAQ":
    
    st.dataframe(dao.select_faq(), use_container_width=True)
    

# v1 = st.sidebar.slider("X", 1, 10)
# st.write("선택된 값: ", f"**{v1}**")
# b = st.text_input("ㅎㅇ")
# v2 = st.sidebar.text_input("이름")
# st.write("이름: " + f"**{v2}**")

# v3 = st.sidebar.radio(
#     "지역선택",
#     ["서울", "인천", "부산"],
#     captions=["2020", "2020", "2023"],
#     index=None,  # 아무것도 선택되지 않도록 한다.
# )

# st.write(f"선택한 지역: **{v3}**")