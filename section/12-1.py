# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('/home/runner/Fastcam-py/resource/database.db', isolation_level=None)

# Cursor 
c = conn.cursor()
print('Cursor Tpye :',type(c))

# 테이블 생성(Data Type : Text, Numeric Integer Real Blob)
# 만약 users 테이블이 없으면 생성하라 
# id 는 int형 개인키, 테이블의 값과 형식
c.execute("CREATE TABLE IF NOT EXISTS users(id INTERGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# ? 처리 된 것은 뒤의 포매팅값을 가져와서 넣어준다
# now 이후 , 는 도대체 머임? 튜플 형태로 만들기 위함?
c.execute("INSERT INTO users VALUES(1, 'bkwag', 'bkwag@naver.com', '010-1111-2345', 'bkwag.git', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# 한번에 여러개 삽입 (튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
#conn.execute("DELETE FROM users")
# 몇개 지운지 나온다 
# print("users db deleted: ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()
