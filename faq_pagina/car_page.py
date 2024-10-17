import streamlit as st
from accident.accident_class import CARDao  # FAQDao 클래스 import
import configparser as parser
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import platform

def car_dao():
    props = parser.ConfigParser()  # Parser객체 생성
    props.read("./config.ini")     # ini 파일 읽기
    mysql_config = props['MYSQL']  # MYSQL Section "[MYSQL]"의 설정정보 조회
    
    cars = CARDao(
        mysql_config['host'],
        3306, 
        mysql_config['user'],
        mysql_config['password'],
        mysql_config['db']
    )
    return cars
    
def display_accident(car_dao):
    search_type_option = st.selectbox(
        label="검색 종류",
        options=["선택하기","전체 조회", "그래프 조회"]
    )

    if search_type_option == "전체 조회":
        # 전체 조회 페이징 처리
        # 결과 표시
        st.markdown(f"2023년도 사고 조회")
        total_accident = car_dao.select_all_data()

        sido = "👉🏻시도👈🏻"
        sigungu = "👉🏻시군구👈🏻"
        death_type = "👉🏻사고유형👈🏻"
        
        road1 = "😯일반국도😯"
        road2 = "😯지방도😯"
        road3 = "😯특별광역시도😯"
        road4 = "😯시군도😯"
        road5 = "😯고속도로😯"
        road6 = "😯기타😯"
        
        st.dataframe(total_accident, height=800, width=1300, column_config={"0": sido,"1":sigungu,'2':death_type,'3':road1, '4':road2, '5':road3, '6':road4, '7':road5, '8':road6})
    elif search_type_option == "그래프 조회" :
        make_graph_img()


def make_graph_img() :
    plt.figure()        
    df = pd.read_csv("./accident__.csv", header=[1], thousands=',')
    if platform.system() == "Darwin" :
        rc('font', family='AppleGothic')
    else :
        rc('font', family='Malgun Gothic')

    f, axes = plt.subplots(3, 2)
    f.set_size_inches((20, 15))
    plt.subplots_adjust(wspace = 0.3, hspace = 0.3)


    groups1 = df.groupby(['시도'])['일반국도'].sum()
    axes[0, 0].plot(groups1, alpha = 0.5, color='green')
    axes[0, 0].set_yticks(range(0, 40000, 2000))
    axes[0, 0].legend(['일반 국도 사고'])

    groups2 = df.groupby(['시도'])['지방도'].sum()
    
    axes[0, 1].plot(groups2, alpha = 0.5, color='green')
    axes[0, 1].set_yticks(range(0, 10000, 2000))
    axes[0, 1].legend(['지방도 사고'])
    
    groups3 = df.groupby(['시도'])['특별광역시도'].sum()
    
    axes[1, 0].plot(groups3, alpha = 0.5, color='green')
    axes[1, 0].set_yticks(range(0, 90000, 5000))
    axes[1, 0].legend(['특별광역시도 사고'])
    
    groups4 = df.groupby(['시도'])['시군도'].sum()
    
    axes[1, 1].plot(groups4, alpha = 0.5, color='green')
    axes[1, 1].set_yticks(range(0, 70000, 5000))
    axes[1, 1].legend(['시군도 사고'])
    
    groups5 = df.groupby(['시도'])['시군도'].sum()
    
    axes[2, 0].plot(groups5, alpha = 0.5, color='green')
    axes[2, 0].set_yticks(range(0, 70000, 5000))
    axes[2, 0].legend(['고속국도 사고'])
    
    groups6 = df.groupby(['시도'])['기타'].sum()
    
    axes[2, 1].plot(groups6, alpha = 0.5, color='green')
    axes[2, 1].set_yticks(range(0, 15000, 2000))
    axes[2, 1].legend(['기타 사고'])

    plt.savefig("graph.png")
    st.image('./graph.png')
    