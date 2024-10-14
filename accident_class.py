# HR 데이터베이스에서 필요한 SQL 작업 처리 모듈
import pymysql
import pymysql.cursors

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
        