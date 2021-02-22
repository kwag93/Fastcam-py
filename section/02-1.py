# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
# 기본 출력
print('Hello Python!')  # 문법적 중요
print("Hello Python!")  # 텍스트 의미
print("""Hello Python!""")
print('''Hello Python!''')

print() 
# 파이선은

# separator 옵션 사용 
print('T', 'E', 'S', 'T', sep='')
# 단어를 sep 기준으로 연결
# TEST 로 연결됌
print('2019', '02', '19', sep='-')
#2019-02-19 가 될것
print('niceman', 'google.com', sep='@')
#niceman@google.com
print() #\n 개행 효과

# end 옵션 사용
print('Welcome To', end=' ')
# 뒤쪽을 기준으로 end 추가 즉 welcome to 공백 the black 으로 이어짐
print('the black parade', end=' ')
print('piano notes')

print() 

# file 옵션 사용
import sys

print('GeeksForGeeks', file=sys.stdout)

print()

print("%s's favorite number is %d" % ('Eunki', int(45))) 
# printf 와 비슷한 방식인듯. %s는 문자열 %d 는 정수

# format 사용
print('{} and {}'.format('You', 'Me')) # 순서대로 들어가게 됌
print('{0} and {1} and {0}'.format('You', 'Me')) # 맵핑과 같다
# you and me and you 가 될것이다
print('{var1} are {var2}'.format(var1='You', var2='Niceman')) #포맷에 완전 지정도가능

# %d, %f, %s
print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) #printf 의 형식지정방식을 다양하게 보여준다
print("Test1: {0:5d}, Price:{1:4.2f}".format(776, 6534.123)) 
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

# \ 의 효과

print("'you") #you
print('\'you\'')  #'you'
print('"you"') # "you"
print("""'you'""") # 'you'
print('\\you\\') # \you\