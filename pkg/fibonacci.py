# 이때 받는 값을 미리 정해놓으면 defalut값이 정해지는것으로 값이 안들어올때 해당 값을 참조한다
class Fibonacci:
    def __init__(self, title="Fibonacci"):
        self.title = title
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a,b = b, a+b
        print()

    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a,b = b, a+b
        return result