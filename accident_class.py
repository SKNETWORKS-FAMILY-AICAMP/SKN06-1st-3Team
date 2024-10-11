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
        insert_sql = """insert into accident (accident_idx, si_idx, sigungu_name, death_idx, national_road_province, special_metropolitan_city, 
        city_county, high_speed_national_highway, etc) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.executemany(insert_sql, data)
                conn.commit()
        print("사고 수:", len(data))
        print("삽입된 값들:", data)


    def insert_sido (_self, data) :
        sql = "INSERT INTO sido (location) VALUES (%s)"
        with _self.get_connection() as conn:
            with conn.cursor() as cursor:
                cnt = cursor.executemany(sql, data)  # executemany() 결과 행수 반환.
                conn.commit()
        
        print("insert된 총 행수:", cnt)