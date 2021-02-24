# 파이썬 모듈과 패키지

# 상대 경로 기준 .. / . 
# .. 부모 디렉토리
# . 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci
Fibonacci.fib(300)

# 사용2(클래스) 메모리를 많이 먹음
from pkg.fibonacci import *
Fibonacci.fib(300)

# 사용3(클래스) as 즉 별칭
from pkg.fibonacci import Fibonacci as fib
fb.fib(100)

# 사용4(함수)
import pkg.calculations as c
print(c.add(10, 100))

# 사용5(함수) 특정 함수만 가져와서 사용
from pkg.calculations import div as d 

# 사용6 
import pkg.prints as p 
import builtins # 기본으로 자동
p.prt1()
p.prt2()
print(dir(builtins))