# Section07-1
# 파이썬 클래스 이해
# self, 클래스, 인스턴스 변수

# 클래스와 인스턴스의 차이
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 선언 
# class 클래스명:
#     함수
#     함수
#     함수
# 예를 들어 학생 클래스에 관련 성적관리등의 함수를 모아놓는다

# 예제1 클래스는 첫글자가 대문자여야한다. 카멜케이스
class UserInfo:
    # 속성, 메소드로 구성되어있음
    # 초기화함수
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)
# 인스턴스화
# 네임스페이스에 각자 다른 값이 들어가있음
user1 = UserInfo("bkwag")
user1.user_info_p()
user2 = UserInfo("park")
user2.user_info_p()
# 두개의 값이다른것을 확인 가능함

# id는 메모리의 주소값을 찍어준다
# 두 변수가 다른 네임스페이스를 사용하고 있음을 확인가능
print(id(user1))
print(id(user2))
# 네임스페이스 출력
print(user1.__dict__)
print(user2.__dict__)

# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('fun1 called!')
    def func2(self):
        print('fun2 called')

a = SelfTest()
# a.func1() 은 출력이 안됌. self로 들어가는 인스턴스화가 없기 때문 셀프가 없으면 클래스에서 직접 불러야한다
SelfTest.func1()
a.func2()

print(id(a))

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('bkwag')
user3 = WareHouse('soocho')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) 
# 클래스 네임스페이스, 클래스 변수를 공유중이다
# 모두 사용중임을 확인 가능

# 인스턴스는 공유하지 않음
print(user1.name)
print(user2.name)
print(user3.name)

# 하나의 변수로 모두가 공유가능
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1 # 인스턴스 삭제
print(user2.stock_num)
print(user3.stock_num)
# user1 이 사라져서 2를 출력하는 모습을 볼수있음