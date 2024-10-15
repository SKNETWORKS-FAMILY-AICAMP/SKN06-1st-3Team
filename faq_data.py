import pymysql
import FAQ.faq_class as FAQDao
import configparser as parser


def get_dao():
    props = parser.ConfigParser() # parser 생성
    props.read("config.ini") # ini 파일 읽기
    config = props['MYSQL'] # section이름으로 읽기
    dao = FAQDao.FAQDao(host=config['host'], port=3306, user=config['user'], 
                        password=config['password'], db=config['db'])
    result = 0
    result += dao.faq_data_kia()
    result += dao.faq_data()
    result += dao.faq_data_hyundai()
    return result

get_dao()