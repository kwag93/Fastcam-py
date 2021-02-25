# 파일 읽기, 쓰기
# 읽기: r 쓰기(기존 파일 삭제): w 추가(파일 생성 또는 추가): a(append)
# 예제1
f = open('../resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))
# 항상 다 쓰고나면 close를 해주어야 한다. 
f.close()

print('-----------------------------')
# 예제2
# with문이 끝나면 자동으로 리소스를 반환
with open('../resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('-----------------------------')
print('-----------------------------')

# 예제3
# 공백 삭제 strip
with open('../resource/review.txt','r') as f:
    for c in f:
        print(c.strip())

print()
print()

# 예제4
# 한번 쭉 읽어 eof까지 진행된 상태이기 때문
with open('../resource/review.txt','r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용없음 eof임
    print(">", content)

# 예제5
# 한줄씩 가져오는 readline
with open('../resource/review.txt','r') as f:
    line = f.readline()
    while line:
        print(line, end='# ')
        line = f.readline()

# 예제6
# \n 기준으로 리스트 형태로 가져온다
with open('../resource/review.txt','r') as f:
    content = f.readlines()
    print(content)
    for c in content:
        print(c, end= ' ***** ')

print()
print()

# 예제 7

score = []
with open('../resource/score.txt','r') as f:
    for line in f:
        score.append(int(line)) # 문자열로 가져옴 형변환
    print(score)

print('Average: {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('../resource/text1.txt','w') as f:
    f.write("Hellow Py")
with open('../resource/text1.txt','a') as f:
    f.write("Good day\n")

# 예제2
from random import randint
with open('../resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제3
# writelines : 리스트를 파일로 저장
with open('../resource/text3.txt','w') as f:
    list = ['bkwag\n', 'park\n', 'joo\n']
        f.writelines(list)

# 예제4
# 파일을 연결해주면 파일에 바로 쓸 수 있음. 
with open('../resource/text4.txt','w') as f:
    print("Test content1", file=f)

