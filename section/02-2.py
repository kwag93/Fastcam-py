# import this  이는 # 다음 띄어쓰기 하는것이 문법이다 (주석)
import sys

# 파이썬 기본 인코딩 
print(sys.stdin.encoding)
print(sys.stdout.encoding) # 이를 통해 입 출력이 utf-8로 진행되고 있음을 확인 가능

# 출력문
print('My name is bkwag!')

# 변수 선언
myName = 'bkwag'

# 조건문
if myName == 'bkwag':
    print('ok') # 들여쓰기 즉 indent 자체가 문법이다

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), (i*j)) # 여기서 , i * j 를 했을때 값이 나오는부분? 
        #자동으로 뒤에 추가됨을 확인 가능

# 변수선언 한글로도 가능

# 함수 선언

def greeting():
    print("안녕하세요. ",myName) # 이 경우에도 뒤에 자동으로 변수 myname이 나왔다
greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))