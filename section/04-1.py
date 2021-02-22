# 데이터 타입

v_str1 = "Hi"
v_bool = False
v_str2 = "bkwag"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "bkwag", # key와 value 를 나눔. "" 안의 값은 문자열이다
    "age" : 29
}

v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {3, 5, 7}

print(type(v_list)) # type 안에 값을 넣으면 어떤 타입인지 확인이 가능하다

i = 30
j = 10
f1 = 1.234
f2 = 123.123

print(f1 ** f2) # 단순한 곱셈이 아닌 제곱을 하는것
print(f1 + i) # 자동 형변환이 진행되어 실수값이 나온다

# 형변환
re = j + f1
# complex 는 복소수 임
# int true는 1 false는 0으로 변환해줌
print(complex(False)) # 0j로 나온다

# 단항연산자
y = 100
y += 100

# math 함수
n, m = divmod(100, 8)
print(n, m) # 몫은 n 으로 나머지는 m 으로 들어간다

import math 

print(math.ceil(5.1)) # 5.1이상인 정수 6
print(math.floor(5.1)) # 5.1 이하인 정수 5