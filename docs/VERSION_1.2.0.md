
## ParaView Evaluator
```
1. ParaView 설치
2. 환경 변수 설정 <code>C:\Program Files\ParaView 5.13.1\bin</code> -> <code>pvpython</code>
3. config.json 설정 데이터 경로, 시나리오 설정
    데이터 경로 구분자는 무조건 '/'로 되어있어야 함.
4. pvpython main.py 명령어 실행
```
## VisIT Evaluator
1. 환경변수-User 변수에 PYTHONPATH 만들고, C:\Users\User\LLNL\VisIt3.4.2\lib\site-packages\visit 추가
2. 환경변수-시스템 변수에 Path에서 Python 3.9버전 경로 추가
```
# Move path where exists main_visit.py
# Should modify config.json 'vis', 'Interact' or 'Screenshot'
config.json 설정 데이터 경로, 시나리오 설정
    데이터 경로 구분자는 무조건 '/'로 되어있어야 함.
visit -cli -s main_visit.py # no Screenshots
visit -cli -s -nowin main_visit.py # Screenshots
```