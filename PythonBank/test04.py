m = 0
n = 1

def func():
    global m, n # 전역변수 사용 위해
    m = m + 1
    n += 1

func()
print(m, n)

# 중첩함수
def counter(max):
    t = 0

    def output(): # counter 함수 내에서만 사용 가능
        print('t = {0}'.format(t))

    while t < max:
        output()
        t += 1

counter(10)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(9))

# lambda
a = lambda x, y : x * y
print(a(2, 8))

# Closure:대리자
def calc(a):
    def add(b):
        return a + b
    return add

sum = calc(1)
print(sum(2))