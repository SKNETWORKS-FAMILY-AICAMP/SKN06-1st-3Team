import streamlit as st
import faq_class as FAQDao
import configparser as parser

st.set_page_config("FAQ", layout="wide")
def get_dao():
    props = parser.ConfigParser() # parser 생성
    props.read("config.ini") # ini 파일 읽기
    config = props['MYSQL'] # section이름으로 읽기
    dao = FAQDao.FAQDao(host=config['host'], port=3306, user=config['user'], 
                        password=config['password'], db=config['db'])
    return dao

dao = get_dao()

def get_faq():
    return (('all', 'all'),) + dao.select_category()


by = st.sidebar.radio(
    "검색기준 선택",
    ["category","제목"],
    index=None
)

category_option = title_option = None
if by == "category":
    category_option = st.sidebar.selectbox(
        label="Category입력",
        options=get_faq(),
        format_func=lambda x: x[0]
    )
    title_option = None
elif by == "제목":
    title_keyword = st.sidebar.text_input("제목을 입력해주세요.")

    category_option = None
    

if category_option and "all" not in category_option:
    df = dao.select_faq_by_category(category_option[0])
    keyword = f"**{category_option[0]}** category - {len(df)} 개"
elif title_keyword:
    df = dao.select_faq_by_title(title_keyword)
    keyword = f"**{title_keyword}** 제목으로 검색한 결과 - {len(df)} 개"
st.title("검색 결과")
try:
    st.markdown(keyword)
    st.dataframe(df, use_container_width=True)
except:
    st.subheader("검색조건입력")