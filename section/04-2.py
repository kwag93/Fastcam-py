# 문자열

str1 = "Hi bkwag"
str2 = str('')
print(len(str2))

# raw string( 이스케이프 문에 영향을 받지 않는다 파일경로에 많이 사용됌)
normal_string = "C:\Programs\example\n"
raw_string = r'C:\Programs\example\n'
 
print(normal_string)
print(raw_string)

#output:
# C:\Programs\example
 
# C:\Programs\example\n

# 멀티라인
# 개행 문자열을 넣지 않아도 개행을 표현할 수 있음 이때 \가 개행을 막는 역할을 해줌
str3 = \
"""
문자열
테스트
"""
print(str3) 

# 연산

# 곱하기는 여러번 반복
# 더하기는 문자열이 합쳐진다
# 단 더하기에 int형을 주면 에러가 난다

# in 연산자
print('a' in str1) # a문자가 포함되어 있는지 체크 true or false로 나온다

# 문자열 형 변환
print(type(str(77)))

# 다양한 문자열 함수

# capitalize 는 첫글자만 대문자로 바꾸어준다
print(str1.isalnum) # is ~~ 로 시작하는 다양한 함수
print(str1.replace('hi', 'hiii')) #변환 함수
print(list(reversed(str1))) #list로 선언해서 사용해주어야 거꾸로 출력된다. 슬라이싱 추천

a = 'bwkag'
b = 'apple'

# 문자열 슬라이싱

print(a[0:3]) # bwk
print(a[0:len(a)]) # 0부터 끝까지
print(a[:4]) # 공백부분이 처음부터로 인식됌
print(b[0:4:2]) # 0~4까지 가고 2개씩 건너뛰자 즉 a, p, l중 4까지라 p까지만 진행됐다
print(b[1:-2]) # -는 뒤를 의미한다 즉 1인 p 에서 -2인 p까지 
print(b[::-1]) # 마치 reverse처럼 출력하는것. 