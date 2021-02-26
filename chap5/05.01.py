# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print('EX1-1 -')
print(dir())

# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)
# y 값을 변경해도 x 가 변경되는 상황임을 확인 가능하다
x['class'] = 10
print('EX2-5 -', x, y)

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z) # 같은 객체
# is 메서드로 비교하는게 제일 빠르다
print('EX2-8 -', x is not z) 
print('EX2-9 -', x == z) # 값이 같다

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
# 튜플은 불변이기 때문에 값이 같아도 다른 것이다
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2) # TRUE 
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3) # FALSE 아이디가 같지는 않음을 확인 가능
# 즉 값은 같더라도, 그 메모리 값이 같지 않을 수 있음

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체 새로 생성) 튜플은 불변이기 때문이다
print('EX4-10 -', tl3)
# print(id(tl1[2]))
# 리스트 안에 튜플을 넣는것은 위험하다는걸 알려준다
print()
print()

# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy
# 복사를 도와주는 패키지

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
# 3개의 ID 가 모두 다르다는것을 알 수 있음. 객체를 복사했기 때문이다
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))
# 1, 2 는 같고 3은 다르다. 즉 1,2는 얕은복사가 되어 LINK형태로 되어있는 것이고 3은 깊은 복사가 진행된것이다
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)

print('EX6-2 -', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경 안됨

# 리스트와 튜플을 골라서 사용

# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
# 같은 ID
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
# 같은 ID 참조하는 위치가 같다
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))