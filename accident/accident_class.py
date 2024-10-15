# HR 데이터베이스에서 필요한 SQL 작업 처리 모듈
import pymysql
import pymysql.cursors

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

class CARDao:
    def __init__(_self, host:str, port:int, user:str, password:str, db:str):
        _self.host = host
        _self.port = port
        _self.user = user
        _self.password = password
        _self.db=db
        

    def get_connection(_self) -> pymysql.Connection:
        return pymysql.connect(host=_self.host, port=_self.port, user=_self.user, password=_self.password, db=_self.db)
        
    def insert_accident_data(_self, data):
        insert_sql = """insert into accident (si_idx, sigungu_idx, death_idx, normal_road, national_road_province, special_metropolitan_city, 
        city_county, high_speed_national_highway, etc) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.executemany(insert_sql, data)
                conn.commit()
        print("사고 수:", len(data))


    def insert_sido (_self, data) :
        sql = "INSERT INTO sido (location) VALUES (%s)"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cnt = cursor.executemany(sql, data)  # executemany() 결과 행수 반환.
                conn.commit()

    def insert_sigungu(_self, data) :
        sql = "INSERT INTO sigungu (si_idx, sigungu_name) VALUES (%s, %s)"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, data)
                conn.commit()
                
    def insert_death_type(_self, data) :
        sql = "INSERT INTO death_type (acc_level) VALUES (%s)"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.executemany(sql, data)
                conn.commit()
        

    def select_si(_self, location) :
        f_sql = "SELECT si_idx FROM sido WHERE location = %s"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f_sql, location)
                si_idx = cursor.fetchone()
        return si_idx


    def select_sigungu(_self, location) :
        f_sql = "SELECT sigungu_idx FROM sigungu WHERE sigungu_name = %s"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f_sql, location)
                sigungu_idx = cursor.fetchone()
        return sigungu_idx


    def select_death_type(_self, acc_level) :
        f_sql = "SELECT d_idx FROM death_type WHERE acc_level = %s"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f_sql, acc_level)
                d_idx = cursor.fetchone()
        return d_idx

    def select_all_data(_self) :
        sql = '''select location, sigungu_name, acc_level, normal_road , national_road_province, special_metropolitan_city, city_county, high_speed_national_highway, etc from  accident a 
                join sido s on s.si_idx = a.si_idx 
                join sigungu s2 on s2.sigungu_idx = a.sigungu_idx 
                join death_type dt on dt.d_idx = a.death_idx
                order by a.accident_idx ASC'''
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                res = cursor.fetchall()
        return res

    def select_graph(_self) :
        df = pd.read_csv("./accident__.csv", header=[1], thousands=',')
        
        plt.figure()
        rc('font', family='AppleGothic')


        # Add histogram data
        groups1 = df.groupby(['시도'])['일반국도'].sum()
        groups2 = df.groupby(['시도'])['지방도'].sum()
        groups3 = df.groupby(['시도'])['특별광역시도'].sum()
        
        # Group data together
        hist_data = [group1, group2, group3]
        
        group_labels = ['Group 1', 'Group 2', 'Group 3']
        
        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])
        
        # Plot!
        st.plotly_chart(fig, use_container_width=True)

        
        # groups1 = df.groupby(['시도'])['일반국도'].sum()
        
        # axes[0, 0].plot(groups1, alpha = 0.5, color='green')
        # axes[0, 0].set_yticks(range(0, 40000, 2000))
        # axes[0, 0].legend(['일반 국도 사고'])
        
        # groups2 = df.groupby(['시도'])['지방도'].sum()
        
        # axes[0, 1].plot(groups2, alpha = 0.5, color='green')
        # axes[0, 1].set_yticks(range(0, 10000, 2000))
        # axes[0, 1].legend(['지방도 사고'])
        
        # groups3 = df.groupby(['시도'])['특별광역시도'].sum()
        
        # axes[1, 0].plot(groups3, alpha = 0.5, color='green')
        # axes[1, 0].set_yticks(range(0, 90000, 5000))
        # axes[1, 0].legend(['특별광역시도 사고'])
        
        # groups4 = df.groupby(['시도'])['시군도'].sum()
        
        # axes[1, 1].plot(groups4, alpha = 0.5, color='green')
        # axes[1, 1].set_yticks(range(0, 70000, 5000))
        # axes[1, 1].legend(['시군도 사고'])
        
        # groups5 = df.groupby(['시도'])['시군도'].sum()
        
        # axes[2, 0].plot(groups5, alpha = 0.5, color='green')
        # axes[2, 0].set_yticks(range(0, 70000, 5000))
        # axes[2, 0].legend(['고속국도 사고'])
        
        # groups6 = df.groupby(['시도'])['기타'].sum()
        
        # axes[2, 1].plot(groups6, alpha = 0.5, color='green')
        # axes[2, 1].set_yticks(range(0, 15000, 2000))
        # axes[2, 1].legend(['기타 사고'])
        
        # res = plt.show()
        # return res