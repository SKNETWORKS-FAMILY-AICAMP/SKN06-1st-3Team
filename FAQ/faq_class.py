import pymysql
from crawling import crawl_data 

class FAQDao:
    def __init__(self, host:str, port:int, user:str, password:str, db:str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db=db

    def get_connection(self) -> pymysql.Connection:
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    # Category 이미 존재하는지 확인
    def is_category_equals(self, category):
        check_sql = 'SELECT 1 FROM category WHERE category = %s'
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(check_sql, category)
                return cursor.fetchone() is not None # 카테고리가 존재하면 True 반환
    # Insert Category
    def insert_category(self, category):
        insert_sql_category = "INSERT INTO Category (category) VALUES (%s)"
        try:
            # DB연결
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    #중복되지 않는 값만 삽입
                    categorys = [categorys1 for categorys1 in category if not self.is_category_equals(categorys1)]
                    if categorys: # 카데고리가 있을 떄만 삽입
                        # 다중 삽입
                        result = cursor.executemany(insert_sql_category, categorys)
                        conn.commit() # 커밋
                        return result
                    else:
                        return 0
        except Exception as e:
            print(f"DB 삽입 중 에러 발생 : {e}")
        return None
        
    # FAQ 같은 값이 존재하는지 확인
    def is_faq_equals(self, category, title, content):
        check_sql = "SELECT 1 FROM faq WHERE category = %s AND title = %s AND content = %s"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(check_sql, (category, title, content))
                return cursor.fetchone() is not None
                
    # Insert FAQ
    def insert_faq(self, data):
        insert_sql = "INSERT INTO faq(category, title, content) VALUES (%s, %s, %s)"
        try:
            # DB연결
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    # 중복되지 않는 값만 삽입
                    faqs = [faq for faq in data if not self.is_faq_equals(faq[0], faq[1], faq[2])]
                    if faqs: # faq가 있을 때만 삽입
                        # 다중 삽입
                        result = cursor.executemany(insert_sql, faqs)
                        conn.commit() # 커밋
                        return result
                    else:
                        return 0
        except Exception as e:
            print(f"DB 삽입 중 에러 발생 : {e}")
        return None

    def faq_data(self):
        crawled_data = crawl_data() 
        # crawling한 데이터 category만 추출
        category = list(set([faq[0] for faq in crawled_data]))
        # category Table에 데이터 삽입
        result = self.insert_category(category)
        # FAQ Table에 데이터 삽입
        result2 = self.insert_faq(crawled_data)
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