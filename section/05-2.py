# 반복문

# for , while

v1 = 1
while v1 < 11:
    print("v1 is:", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is:",v2)

for v3 in range(1, 11):
    print("v3 is :", v3)

# 1~100까지의 합

sum1 = 0
cnt = 1

while cnt <= 100:
    sum1 += cnt
    cnt += 1

print(sum1)
print('1 ~ 100 : ',sum(range(1, 101)))
print('1 ~ 100 :',sum(range(1, 101, 2))) 
# 두칸씩 띄워서 더해줌

# 순서가 있는(시퀀스) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리 반복
# iterable : range, reversed, enumerate, filter, map, zip
print()
print() 

names = ["bkwag", "park", "kim", "choi"]

for name in names:
    print(name)

word = "dreams"

for s in word:
    print(s)

my_info = {
    "name" : "bkwag",
    "age" : 29,
    "city" : "seoul"
}

for key in my_info:
    print(key)
# 기본은 key만 가져옴
for key in my_info.values():
    print(key)

for key in my_info.keys():
    print(key)
# 기본으로 가져오니 사용하지 않아도 됌
for key in my_info.items():
    print(key)
# items 즉 값을 전부 가져옴

name = "kennRY"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 2, 1, 38, 33]

for num in numbers:
    if num == 33:
        print("found!")
        break
    else:
        print("not found")
else:
    print("Not Found 33")
# 끝까지 돌고나면 else에 들어감. break가 수행된다면 거기서 끝나고 else는 작동하지 않음

# continue

lt = ["1" , 2, 5, True, 4.3, complex(4)]

for x in lt:
    if type(x) is float:
        continue
    print("타입 :", type(x))
 # countinue를 만나면 바로 아래의 라인이 실행되지않음

name1 = "Himan"
print(reversed(name1)) #주소가 나옴
print(list(reversed(name1)))
print(tuple(reversed(name1)))