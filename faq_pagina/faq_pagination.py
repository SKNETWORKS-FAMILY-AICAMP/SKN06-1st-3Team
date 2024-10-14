import streamlit as st
from FAQ.faq_class import FAQDao  # FAQDao 클래스 import
import configparser as parser
def get_dao():
    props = parser.ConfigParser()
    props.read("config.ini")
    config = props['MYSQL']
    dao = FAQDao(host=config['host'], port=3306, user=config['user'], password=config['password'], db=config['db'])
    return dao

# 카테고리 목록을 가져오는 함수
def get_category_options(dao):
    categories = dao.select_category()  # 카테고리 목록을 가져옴
    return [category[0] for category in categories]  # 리스트로 변환

# FAQ 관련 기능을 처리하는 함수
def display_faq_section(dao):
    search_type_option = st.selectbox(
        label="검색 종류",
        options=["선택하기","전체 조회", "카테고리 검색", "제목 검색", "내용으로 검색"]
    )

    if search_type_option == "전체 조회":
        # 전체 조회 페이징 처리
        total_faqs = dao.select_faq_count()[0]
        items_per_page = 10
        total_pages = max((total_faqs // items_per_page) + 1, 1)  # 최소 페이지 수는 1

        # 페이지가 1개 이상일 때만 슬라이더 표시
        if total_pages > 1:
            page = st.slider("Page", 1, total_pages)
        else:
            page = 1  # 페이지가 1개라면 슬라이더 없이 1로 설정

        offset = (page - 1) * items_per_page
        faqs = dao.select_faq(limit=items_per_page, offset=offset)

        st.markdown(f"**현재 Page {page}** - 전체 조회 결과 - {len(faqs)}개 (총 {total_faqs}개)")

        # 데이터를 테이블로 표시하지 않고, category와 title을 expander로 표시
        for faq in faqs:
            # faq가 튜플로 되어있을 가능성이 있어 인덱스로 접근
            with st.expander(f"{faq[0]} - {faq[1]}"):  # category는 faq[0], title은 faq[1]
                st.write(faq[2])  # content는 faq[2]에 저장되어 있을 것

    elif search_type_option == "카테고리 검색":
        category_options = get_category_options(dao)
        selected_category = st.selectbox("카테고리 선택", category_options)

        if selected_category:
            total_faqs = dao.select_count_category(selected_category)['COUNT(*)']
            items_per_page = 10
            total_pages = max((total_faqs // items_per_page) + 1, 1)

            if total_pages > 1:
                page = st.slider("Page", 1, total_pages)
            else:
                page = 1 

            offset = (page - 1) * items_per_page

            # 선택된 카테고리의 FAQ 데이터 가져오기
            faqs = dao.select_faq_by_category(selected_category, limit=items_per_page, offset=offset)

            # 결과 표시
            st.markdown(f"**{selected_category}** 카테고리 - 페이지 {page}/{total_pages} - {len(faqs)}개 (총 {total_faqs}개)")

            for faq in faqs:
                with st.expander(f"{faq['category']} - {faq['title']}"): 
                    st.write(faq['content'])

    elif search_type_option == "제목 검색":
        # select_count_title, select_faq_by_title
        input_content = st.text_input("제목 검색")
        if input_content:
            total_title = dao.select_count_title(input_content)['COUNT(*)']
            items_per_page = 10
            total_pages = max((total_title // items_per_page) + 1, 1) 
            if total_pages > 1:
                page = st.slider("Page", 1, total_pages)
            else:
                page = 1
            offset = (page -  1) * items_per_page
            title = dao.select_faq_by_title(input_content, limit=items_per_page, offset=offset)
            st.markdown(f"**{input_content}** 제목 - 페이지 {page}/{total_pages} - {len(title)}개 (총 {total_title}개)")

  
            for faq in title:
                with st.expander(f"{faq['category']} - {faq['title']}"): 
                    st.write(faq['content']) 
    elif search_type_option == "내용으로 검색":
        input_content = st.text_input("내용으로 검색")
        if input_content:
            total_content= dao.select_count_content(input_content)['COUNT(*)']
            items_per_page = 10
            total_pages = max((total_content // items_per_page) + 1, 1) 
            if total_pages > 1:
                page = st.slider("Page", 1, total_pages)
            else:
                page = 1
            offset = (page -  1) * items_per_page
            content = dao.select_faq_by_content(input_content, limit=items_per_page, offset=offset)
            st.markdown(f"**{input_content}** 제목 - 페이지 {page}/{total_pages} - {len(content)}개 (총 {total_content}개)")

            for faq in content:
                with st.expander(f"{faq['category']} - {faq['title']}"): 
                    st.write(faq['content']) 