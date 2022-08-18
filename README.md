## 함수 실행
함수 실행 전에 준비되어야 할 것이 있습니다.
1. 노션 개발자 페이지(`developers.notion.com`)에서 integration 설정을 해야합니다.
2. 분석을 원하는 노션 페이지를 integration과 공유해야합니다.
3. `config` 디렉토리 안에 두 파일을 준비해야합니다.
  * `credentials.txt`: integration 설정 후 받은 api key를 그대로 넣어주셔야합니다.
  * `root.txt`: 루트 블록의 id를 넣어주시면 됩니다.


```shell
# 가상환경 생성
python -m venv myvenv

# 가상환경 실행
source myvenv/bin/activate

# 필요한 라이브러리 설치
(myvenv) pip install -r requirements.txt

# 함수 실행
(myvenv) python main.py

# 가상환경 종료시
(myvenv) deactivate
```