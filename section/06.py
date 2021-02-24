# section06
# 함수식 및 람다(lambda)

# 함수정의방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명()

# 예제1
def hello(world):
    print("hello", world)

hello("bkwag")
# 함수의 위치는 호출보다 선언이 위에있어야함

# 예제2
def hello_return(world):
    val = "hello " + str(world)
    return val
# 다른 형식이 들어와도 계산되게 형변환
str = hello_return("Python")
print(str)

# 예제3 (다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

v1, v2, v3 = func_mul(100)
print(v1, v2, v3)

# 예제4 (리턴형식변환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(lt)

# 예제5
# *args, *kwargs
# 가변인자처리
def args_func(*args):
    for i,v in enumerate(range(10)):
        print(i,v)

args_func('kim', 'kwag' ,'soo')

# kwargs 딕셔너리로 받아옴
def kwargs_func(**kwargs):
    for k , v in kwargs.items():
        print(k, v)

kwargs_func(name1="kim", name2="kwag")

# 전체 혼합
# 가변인자를 제외하고 필수이다
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
# 가변인자를 주지않아서 빈 공간출력

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num + 1000)

nested_func(10000)


# 예제 6
# int형을 받아 list를 출력한다는걸 알려줌
# 이 형식을 지키지 않아도 오류가 나지않지만, 명시적으로 알려줄 수 있음
def func_mul2(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num: int) -> int:
    return num * 10
a = mul_10 #메모리가 나옴
print(a)
# 할당된 모습을 확인할 수 있음

# 람다식은 가독성이 떨어지기 때문에 너무 많이 사용하지말것
# 메모리의 절약, 짧은코드, 간단한 함수의 적용
lambda_mul_10 = lambda num: num * 10

print('lam >>', lambda_mul_10(1))
# 매개변수는 함수도 가능함
def func_final(x,y,func):
    print(x * y * func(10))

# func_final(10,10,lambda_mul_10)

print('>>>', func_final(10, 10, lambda x : x * 1))

