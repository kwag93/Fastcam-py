# 업그레이드 타이핑 게임 제작

import random
import time 

words  = [] # 영단어리스트
n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('../resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
#print(words) # 단어리스트 출력
# input 안의 값은 프롬포트에 출력된다
input("Ready? Press Enter Key!") #Enter Game Start!

start = time.time() 

while n <= 5:
    random.shuffle(words) # 섞어줌
    q = random.choice(words) # 뽑아옴
    print()
    print("*Question # {}".format(n))
    print(q) # 문제 출력

    x = input() # 입력
    print()
    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")
    n += 1 

end = time.time()
et = end - start # 총 시간
et = format(et, ".3f") # 셋째 자리 출력(시간)

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")
print("게임시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass

