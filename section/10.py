# 파이썬 예외처리 이해

# 예외 종류
# 문법적으로는 에러 없지만, 런타임 프로세스에서 발생하는 예외처리
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('ㅅ)
# if 1 (: 이 없는경우)
# x => y ( 존재하지않는 방식)

# NameError : 참조 변수 없음

a = 10
b = 15
#print(c) 없는 c를 부름

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
# print(x[3]) 인덱스가 존재하지 않음

# KeyError 

dic = {'name': 'bkwag', 'Age': 29}
# print(dic['hobby']) 존재하지않음
print(dic.get('hobby')) #get을 사용시 디폴트값 none이 출력된다

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
# print(time.month()) 존재하지 않는 함수

# ValueError : 참조값이 없을때 발생
x = [1, 5]
# x.remove(10)
# x.index(10)

# FileNotFoundError

# f = open('test.txt','r') 존재하지 않는 파일

# TypeError
x = [1,2]
y = (1,2)
z = 'test'
# print(x + y) 다른 타입은 더할 수 없음
# print(x + z) 불가
# 단 명시적 형변환을 사용시 가능
# print(x + list(y))

# 항상 예외가 발생하지 않을 것으로 가정하고 코딩해야함
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행

# 예제 1

name = ['a', 'b', 'c']
try:
    z = 'a'
    x = name.index(z)
    print('{} Found {} in name'.format(z, x+1))
except ValueError:
    print('Not Found')
else:
    print('OK') # 정상 실행시에 작동

# 예제 2

name = ['a', 'b', 'c']
try:
    z = 'a'
    x = name.index(z)
    print('{} Found {} in name'.format(z, x+1))
except: # 모든 에러 처리 
    print('Not Found')
else:
    print('OK') # 정상 실행시에 작동

# 예외3 
# finally는 예외가 발생하지 않아도 무조건 수행

name = ['a', 'b', 'c']
try:
    z = 'a'
    x = name.index(z)
    print('{} Found {} in name'.format(z, x+1))
except ValueError:
    print('Not Found')
else:
    print('OK') # 정상 실행시에 작동
finally:
    print("OK Finally") # 보통 연결을 해제할때 사용해줌

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError # 발생시킴value 에러가 아니지만 사용하게 만들어주는 것
except ValueError as l: # l을 출력하여 보여줄 수 있음
    print(l)
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')

