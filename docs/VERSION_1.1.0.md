# VERSION 1.1.0
## Contributions
1. Python Shell 안 써도 되는 방법을 찾아냄. 애초에 <code>pvpython</code> 실행파일을 ParaView 설치할 때 제공하고 있었음 (<code>pvbatch</code>도 마찬가지)
    * 더 단순한 모듈화 가능
    * 그래도 Python 외장 라이브러리는 사용 불가능, 시도하려면 <a href="https://discourse.paraview.org/t/how-can-i-install-and-import-other-modules-inside-pvpython/3067">빌드 자체를 새롭게 하면서 추가해야 한다</a>는 말이 있었음.
2. ParaView 내부 trace 기능을 활용한 코드 및 측정 시간 상세화

## Install
```
1. ParaView 설치

2. 환경 변수 설정 <code>C:\Program Files\ParaView 5.13.1\bin</code> -> <code>pvpython</code>

3. git clone --branch v1.1.0 https://github.com/drawcodeboy/ParaView-Evaluator.git 명령어 실행

4. config.json 설정 데이터 경로, 시나리오 설정
    데이터 경로 구분자는 무조건 '/'로 되어있어야 함.

5. pvpython main.py 명령어 실행
```