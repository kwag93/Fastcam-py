# 상속 , 다중상속

# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능
# 상속기본

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 클래스
# 공통으로 쓰는 속성은 부모에서 받고 자식에서 각자 필요한것을 생성하여 사용한다

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type =tp
        self.color = color
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    def show(self):
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)
    # 일반 사용
#  인스턴스 생성
# 상속받은 모습들

model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) # super
print(model1.type) # super
print(model1.car_name) #sub
print(model1.show()) #super
print(model1.show_model()) #sub
print(model1.__dict__)

# Method Overriding( 오버라이딩 )
model2 = BenzCar('22d', 'suv', 'black')
print(model2.show()) # 오버라이딩되어 자식클래스의 값이 출력됌

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
# benz 에 부모 함수인 show를 한번 더 불러서 출력해줌
print(model3.show())

# 상속관계가 깊을경우. 표현해주는 메소드
# Inheritance Info
print(BmwCar.mro())
print(BenzCar.mro())

# 다중 상속
print()
print()

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X, Y):
    pass
class B(Y, Z):
    pass
class M(B, A, Z): 
    pass

print(M.mro())