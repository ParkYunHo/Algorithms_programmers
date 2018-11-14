< PyCharm >
1. git clone 한 뒤에 해당 프로젝트 열기
2. File > Settings > Project > Project Interpreter에서 python path 설정
- gitignore파일로 모드 설정을 무시했으므로
- 해당 Code의 Interpreter가 python임을 설정해야 한다.
3. Run > Edit Configuration 에서 "+"버튼을 클릭해서 Configuration 설정
- Name : Run할때의 이름
- Script path : 실행할 python file (main file)의 path를 설정
- Environment variables, python interpreter : 자동으로 설정됨
- Working directory : clone한 프로젝트 폴더의 path를 설정한다.