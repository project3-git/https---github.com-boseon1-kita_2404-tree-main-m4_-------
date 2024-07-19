import os

# 현재 파일의 정대 경로를 기반으로 basedir 변수를 설정. 이 변수는 프로젝트의 기본 디렉토리를 나타낸다.
# os.path.abspath(path) : 주어진 경로 path의 절대 경로를 반환
# __file__의 디렉토리 부분만믈 추출. D:\kbt_240424\workspace\m4_웹애플리케이션\TodoList_10
basedir = os.path.abspath(os.path.dirname(__file__)) 
# Flask configuration
# 세션 데이터 암호화, CSRF 보호 등을 위해 사용

class Config:
    SECRET_KEY = '2a7eae0acf7d3b42700ccb75dae609d2088b9e2e076e4e4e'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bs:bs@localhost:3306/bs_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_FILES_DEST = os.path.join(basedir,'uploads')


# Uploade configuration
# 파일 업로드 시 저장할 기본 경로를 설정 