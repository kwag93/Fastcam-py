# 딕셔너리

# 순서 없음 중복 불가, 수정가능, 삭제가능
# key, value 형식으로 이루어짐
# 선언
a = {'name': 'bkwag', 'Phone' : '010-0000-0000'}
# key를 중복으로 허용하지 않음 vlaue는 중복이 가능
b = {0: 'Hello a', 1: 'Hello b'}
# 보통 key값을 숫자로 두지는 않음
c = {'arr': [1,2,3,4,5]} 
# 리스트를 사용이 가능함

#출력
print(a['name'])
print(a.get('name'))
# get으로 가져오기도 가능하다.
print(a.get('address'))
# 존재하지 않아서 None
print(c['arr'][1:3])
# 리스트도 잘 가져오는 모습

# 딕셔너리 추가
a['address'] = 'Seoul'
# 추가가 된 모습. 단 순서가 바뀔 수 있음을 기억
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3)
print(a)
# 모든 형식이 들어가는 모습

# keys, values, items 
# 아이템은 들어가있는 모든 값
print(a.keys()) # key를 리스트로 가져옴 단 인덱스 접근은 불가능 하다
print(list(a.keys()))

tmp = list(a.keys())
print(tmp[1:3])

# keys를 사용하기 위해 임시 변수에 저장한 모습
print()
print(a.values()) # 마찬가지로 values를 가져옴
# 역시 list 형변환을 해야 슬라이싱이 가능

print(a.items()) # 모든 값을 가져온다
print()

print(2 in b) # in을 사용할 수 있음. notin 또한가능
print()
# 집합(set) 순서가 없지만 중복도 없다
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6,7,7,7])
print(c)
# 이때 c 의 7은 중복값이기에 사라져서 출력될것이다

t = tuple(b)
print(t)
l = list(b)
print(l)
# 형변환 된 상황
print()
print() 

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
# 교집합을 보여준다
print(s1 & s2)
# 똑같은 교집합

print(s1 | s2)
print(s1.union(s2))
# 합집합을 의미한다 . 중복원소는 제거됌

print(s1 - s2)
print(s1.difference(s2))
# 차집합. 교차된걸 삭제

# 추가와 제거 가능
s3 = set([7,8,9])
s3.add(10)
# 추가된 상황
s3.add(7) 
# 중복되어 추가되지 않음. 단 에러가 나지는 않음
s3.remove(10)
# 삭제가 된다
