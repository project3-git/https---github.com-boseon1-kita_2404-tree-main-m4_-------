python 가상환경 설정

python --version
where python

가상환경 생성 :
cd my_project
python -m venv myenv

가상환경 활성화:
myenv\Scripts\activate

패키지 설치 및 관리:
pip install requests

가상환경 비활성화:
deactivate

가상환경에 설치된 모든 패키지 목록을 requirements.txt 파일로 저장
pip freeze > requirements.txt

requirements.txt 파일을 사용하여 패키지 설치
pip install -r requirements.txt

Python의 패키지 관리자인 pip을 최신 버전으로 업그레이드하는 명령어
python.exe -m pip install --upgrade pip

Live Server Port 이슈
포트 사용 중인 프로세스 확인
netstat -aon | findstr :5500
프로세스 종료: taskkill /PID 3492 /F
