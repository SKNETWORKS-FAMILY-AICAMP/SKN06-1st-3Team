import pymysql

class FAQDao:
    def __init__(self, host:str, port:int, user:str, password:str, db:str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db=db

    def get_connection(self) -> pymysql.Connection:
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    # Insert Category
    def insert_category(self, category):
        insert_sql_category = "INSERT INTO Category (category) VALUES (%s)"
        try:
            # DB연결
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    # 다중 삽입
                    result = cursor.executemany(insert_sql_category, category)
                    conn.commit() # 커밋
                    return result
        except Exception as e:
            print(f"DB 삽입 중 에러 발생 : {e}")
        return None

    # Insert FAQ
    def insert_faq(self, data):
        insert_sql = "INSERT INTO faq(category, title, content) VALUES (%s, %s, %s)"
        try:
            # DB연결
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    # 다중 삽입
                    result = cursor.executemany(insert_sql, data)
                    conn.commit() # 커밋
                    return result
        except Exception as e:
            print(f"DB 삽입 중 에러 발생 : {e}")
        return None

    def faq_date(self, crawDate):
        # crawling한 데이터 category만 추출
        category = list(set([faq[0] for faq in crawDate]))
        # category Table에 데이터 삽입
        result = self.insert_category(category)
        # FAQ Table에 데이터 삽입
        result2 = self.insert_faq(crawDate)
        # 결과 행수 더하기
        result3 = result + result2
        return result3

    def select_faq(self):
        sql = "select category, title, content from faq"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def select_category(self):
        sql = "select category from category"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def select_faq_by_category(self, category:str):
        sql = """
        SELECT c.category, f.title, f.content 
        FROM category c 
        JOIN faq f ON c.category = f.category
        WHERE c.category LIKE %s
        """
        with self.get_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, [f'%{category}%'])
                result = cursor.fetchall()
                return result