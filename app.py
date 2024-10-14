import streamlit as st
import FAQ.faq_class as FAQDao
import configparser as parser
import accident_class as CARDao

def get_dao():
    props = parser.ConfigParser() # parser 생성
    props.read("config.ini") # ini 파일 읽기
    config = props['MYSQL'] # section이름으로 읽기
    dao = FAQDao.FAQDao(host=config['host'], port=3306, user=config['user'], 
                        password=config['password'], db=config['db'])
    return dao

dao = get_dao()
def search_type():
    return ["전체 조회","카테고리 검색","제목 검색","내용으로 검색"]


cars = CARDao(
    mysql_config['host'],
    3306, 
    mysql_config['user'],
    mysql_config['password'],
    mysql_config['db']
)

def search_function(search_type, input_content):
    if search_type == "카테고리 검색":
        return dao.select_faq_by_category(input_content) 
    elif search_type == "제목 검색":
        return dao.select_faq_by_title(input_content)
def category_lists():
    return dao.select_category()
    
st.set_page_config(page_title="SK06_01_3Tim")
# 그래프 한번 해봄
# k = dao.select_count_category()
# s = [ {b.get('category'):b.get('count(*)')} for b in k]
# st.bar_chart(s)

by = st.sidebar.radio("목록", ["FAQ","DATA"])


if by == "FAQ":
    st.dataframe(dao.select_faq(), use_container_width=True)
    search_type = st.selectbox(
        label="검색 종류",
        options=search_type()
    )

    if search_type == "전체 조회":
        # 전체 FAQ 수를 불러옵니다.
        total_faqs = dao.select_faq_count()[0]

        # 한 페이지에 표시할 항목 수를 설정합니다.
        items_per_page = 10

        # 총 페이지 수를 계산합니다.
        total_pages = (total_faqs // items_per_page) + 1

        # 페이지 슬라이더
        page = st.slider("Page", 1, int(total_pages))

        # OFFSET 계산
        offset = (page - 1) * items_per_page

        faqs = dao.select_faq(limit=items_per_page, offset=offset)

        st.markdown(f"전체 조회 결과 - {len(faqs)}개 (총 {total_faqs}개)")
        st.dataframe(faqs, use_container_width=True)
    else:
        input_content = st.text_input(search_type)
        if input_content:
            st.markdown(f"**{input_content}** 로 검색한 결과 - {len(search_function(search_type,input_content))}개")
            st.dataframe(search_function(search_type,input_content), use_container_width=True)

elif by == "DATA" :
    st.dataframe(cars.select_all_data(), use_container_width=True)

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

