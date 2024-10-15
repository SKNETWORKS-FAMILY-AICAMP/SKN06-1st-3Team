import streamlit as st
from accident.accident_class import CARDao  # FAQDao 클래스 import
import configparser as parser
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import plotly.figure_factory as ff

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
        
        df = pd.read_csv("./accident__.csv", header=[1], thousands=',')
        
        plt.figure()
        rc('font', family='AppleGothic')


        # Add histogram data
        group1 = df.groupby(['시도'])['일반국도'].sum()
        group2 = df.groupby(['시도'])['지방도'].sum()
        group3 = df.groupby(['시도'])['특별광역시도'].sum()
        
        # Group data together
        hist_data = [group1, group2, group3]
        
        group_labels = ['Group 1', 'Group 2', 'Group 3']
        
        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])
        
        # Plot!
        st.plotly_chart(fig, use_container_width=True)