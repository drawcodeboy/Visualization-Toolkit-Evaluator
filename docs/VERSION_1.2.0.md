1. 환경변수-User 변수에 PYTHONPATH 만들고, C:\Users\User\LLNL\VisIt3.4.2\lib\site-packages\visit 추가
2. 환경변수-시스템 변수에 Path에서 Python 3.9버전 경로 추가
3. VSCode에서 PYTHONPATH, Path를 잡지 못 하고 있음 -> 이건 일단 Windows 자체 CMD 쓰자.
* * *
<code>visit_commands.py</code>에 모두 저장해둠
visit -cli를 통해 접속해서 명령어 실행할 것
-nowin 유무 차이에 따라 시간 다른지도 봐야한다.
```
# Should modify config.json 'vis', 'Interact' or 'Screenshot'
visit -cli -s main_visit.py # no Screenshots
visit -cli -s -nowin main_visit.py # Screenshots
```