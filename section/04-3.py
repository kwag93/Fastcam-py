# 리스트 (순서 있음, 중복 있음, 수정 가능, 삭제도 가능)
# 배열과 유사함

#선언

a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'Pen'] # 다른 타입의 값을 넣을 수 있음
e = [10, 100, ['pen', 'Banana']] # 리스트 안에 리스트를 선언도 가능하다

# 인덱싱
print(d[1])# 100
print(d[-1]) # pen
print(d[0]+d[1]) #110
print(e[2][1]) # banana
print(e[-1][-2]) # pen

# 슬라이싱
print(d[0:3]) # 3이 없다고 에러가 나지 않고 최대치까지 나왔음
print(e[2][1:3]) # 이 또한 1 만 존재하기 때문
print(c[1:3]) # 2,3 이 나옴. 슬라이싱은 해당 인덱싱 -1 까지 나오기 때문

# 연산

# 더하기는 붙고, 곱하기는 반복된다 
print(str(c[0]) + 'hi') # 형변환을 하지 않는다면 에러가 난다

# 리스트 수정, 삭제
c[0] = 77
print(c) # 리스트가 변경된 모습

c[1:2] = [100, 1000, 10000]
print(c) # 인덱스 1에 값 3개가 들어감
c[1] = ['a','b','c']
print(c) # 리스트에 리스트가 들어간 상태로 출력됌

#삭제
del c[1]
print(c) # 뒤에가 자동으로 땡겨짐.

print()

# 리스트 함수
y = [5, 2, 1, 3, 5]

y.append(6) # 끝에 추가
y.sort() # 오름차순으로 
y.reverse() # 역순으로
y.insert(2, 7) # 2번 인덱스에 7을 삽입
print(y) # insert와 append의 차이
y.remove(2) # 2번 인덱스가 아닌 숫자 2를 찾아 지웠음 인덱스를 지우려면 del
print(y)
y.pop() # 스택처럼 맨 마지막의 값을 꺼내어 사라지게 함 스택의 LIFO를 기억
# pop은 아무런 원소가 없다면 오류가 난다
print(y)

ex = [88, 77]
y.extend(ex) # 끝에 ex값을 추가해준다 (그렇다면 append와의 차이는?)-> 원소 즉 값으로 추가해줌. 
# append는 리스트 그 자체로 추가해준다

print()
print()
print()

# 튜플 (순서 있음, 중복 가능, 수정안됌, 삭제안됌)

# 중요한 키값이나 변하면 안되는 값들

# 선언
a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2] # 튜플은 삭제가 불가능하다

print(c[2])
print(c[3])

print(c + d) # 확장됌 곱하기도 여러개가 나옴

# 튜플 함수 

z = (5, 1, 2, 3, 4)

print(3 in z) # 값을 찾아본다
print(z.index(5)) # 5의 인덱스 위치를 반환
print(z.count(1)) # 1의 개수를 리턴