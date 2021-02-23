# 조건문 실습
# bool형식

print(type(True)) # 앞에가 대문자인것을 명심

if False:
    print("hi")
else:
    print("hello")

# 관계연산자
# > >= < <= == !=

a = 10
b = 0

print(a == b)
# 관계연산자에 따라서 True False가 나옴

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [] ,(), {} ,0 (빈문자열)

city =""

if city:
    print("hi")
else:
    print("hello")
    # 빈 문자열은 false로 들어가는 모습

# 논리 연산자
# and or not 

a = 100
b = 60
c = 15

print('and: ', a > b and b > c) #and 조건 테스트
print('or :', a > b or c > b)
print('not : ', not a > b) # 반대가 나오는 상황
print(not False) # true가 나옴

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용됌
print('ex1 : ' , 5 + 10 > 0 and not 7 + 3 == 10)
# False 앞에서부터 처리 15 이므로 true 10이 맞으므로 false and 이므로 결과적으로는 False일것이다

score1 = 70
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격")
else:
    print("탈락")
# 다중 조건문
num = 90
# elif 를 사용 else if 가 아님
if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
else:
    print("탈락")

# 중첩 조건문
age = 27
height = 170

if age >= 20:
    if height >= 170:
        print("A등급")
    elif height >= 160:
        print("B등급")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")