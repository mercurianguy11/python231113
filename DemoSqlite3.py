# DemoSqlite3.py

# DDL(Data Definition Language) : 데이터베이스의 객체를 생성, 수정, 삭제하는 언어 (create, alter, drop)
# DML(Data Manipulation Language) : 데이터베이스를 다루는 언어 (select, insert, update, delete)

# 전자성경 => SQLite 무료(open source) 카카오톡도 sqlite 100만건...

# 여기서 사용하려는 SQLite3은 로컬 디스크 기반의 가벼운 데이터베이스 라이브러리이다.
# 이미 안드로이드, 아이폰, 윈도우폰 등에서 많이 사용되고 있다. 
# 콘솔에서 작동하는 코드를 작성하고, 나중에  GUI코드를 붙여서 실행파일로 만들어서 고객에게 배포할 수 있다. 


# sqlite3 모듈: 데이터베이스 연결과 같은 전역적인 함수가 정의되어 있다.
# sqlite3.connect(database[, timeout, isolation_level, detect_types, factory]) : SQLite3 DB에 연결하고 연결된 Connection객체를 반환한다. 
# database -> 파일명.db
# .NET 진영 : Connection, Command, DataSet Class
# java 진영 : Connection, Command, ResultSet Class
# python 진영 : Connection, Cursor Class

# sqlite3.complete_statement(sql) : 세미콜론으로 끝나는 SQL 문에 대해 True를 반환한다. 
# sqlite3.register_adapter(type, callable) : 사용자정의 파이썬 자료형을 SQLite3에서 사용하도록 등록한다. 
# sqlite3.register_converter(typename, callable) : SQLite3에 저장된 자료를 사용자정의 자료형으로 변환하는 함수를 등록한다. 


# Connection 클래스 : 연결된 데이터베이스를 동작시키는 역할을 한다. 
# Connection.cursor() : 커서 객체를 생성한다.
# Connection.rollback() : 지금까지 작업한 내용을 DB에 반영하지 않고 트랜잭션 이전 상태로 되돌린다.
# Connection.commit() : 지금까지 작업한 내용을 DB에 반영한다. 
# Connection.close() : DB연결을 종료한다. 
# Connection.execute(sql[, parameters]) : 임시 Cursor객체를 생성해 해당 execute 메서드를 실행한다. 


# Cursor 클래스 : 실질적으로 데이터베이스에서 SQL문장을 실행하고 조회된 결과를 가져오는 역할을 한다. 
# Cursor.execute(sql[, parameters]) : SQL문장을 실행한다. 
# Cursor.executemany(sql, seq_of_parameters) : 동일한 SQL문장을 매개변수만 변경하면서 실행한다. 
# Cursor.executescript(sql_script) : 세미콜론으로 구분된 SQL문장을 실행한다. 
# Cursor.fetchone() : 조회된 결과로부터 데이터 1개를 반환한다.
# Cursor.fetchmany([size=cursor.arraysize]) : 입력 받은 size만큼의 데이터를 리스트 형태로 반환한다.
# Cursor.fetchall() : 조회된 결과 모드를 리스트로 반환


# 데이터베이스 연결 : 물리적인 DB파일이 없으면 생성되며, 파일이 이미 존재하면 그 DB파일을 사용한다. 
# SQL문 실행 : SQL문을 실행한다. 




# 파이썬으로 작성한 프로그램에서 데이터를 관리하는 경우
# 제품 리스트를 입력,수정,삭제,조회를 할 수 있는 파이썬 프로그램 
# 고객 리스트를 입력,수정,삭제,조회를 할 수 있는 파이썬 프로그램
# 웹에서 수집한 데이터를 로컬 데이터베이스에 입력해서 지속적으로 사용해야 하는 경우
# 개발자가 직접 파일 구조를 만들어서 작업하기에는 부담스럽기 때문에 로컬 데이터베이스 엔진을 사용하면 작업량이 줄어든다

# import sqlite3
# con = sqlite3.connect("c:\\work\\test.db")
# con = sqlite3.connect(":memory:")
# cur = con.cursor()
# cur.execute("create table PhoneBook (Name text, PhoneNum text);")
# cur.execute("insert into PhoneBook values('derick','010-222');")