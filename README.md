## 준비
함수 실행 전에 준비되어야 할 것이 있습니다.
1. 노션 개발자 페이지(`developers.notion.com`)에서 integration 설정을 해야합니다.
2. 분석을 원하는 노션 페이지를 integration과 공유해야합니다.
3. `config` 디렉토리 안에 두 파일을 준비해야합니다.
    * `credentials.txt`: integration 설정 후 받은 api key를 넣어주셔야합니다.
    * `root.txt`: 루트 블록의 id를 넣어주시면 됩니다(현재 example로 들어있습니다).


## 함수 실행
함수 실행을 위해서는 위 준비 과정을 모두 마친 후 터미널에서 아래와 같은 순서로 명령어를 입력합니다.
```shell
# 가상환경 생성
python -m venv myvenv

# 가상환경 실행
source myvenv/bin/activate

# 함수 구동에 필요한 라이브러리 설치
(myvenv) pip install -r requirements.txt

# 함수 실행
(myvenv) python main.py

# 실행 완료 후 가상환경 종료시
(myvenv) deactivate
```