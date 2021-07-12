# 구문 테스트

# initialize
n = 0

# Loop
while True:
    n = n + 1
    if (n == 100):
        break
    # n이 짝수라면 출력할 것
    if ((n % 2) == 0):
        print(n)
a = 100
b = 80

if a > b:
    print('max is {0}'.format(a))
else:
    print('max is {0}'.format(b))

i = -45

if i > 0:
    print("{0} is positive".format(i))
elif i == 0:
    print("{0} is zero".format(i))
else:
    print("{0} is negative".format(i))

for u in [0, 1, 2, 3, 4]:
    print('{0} * 3 = {1}'.format(u, u*3))

for i in range(5):
    print(i * 2)

m = 0
while True:
    m = m + 2
    if (m == 20):
        continue

    if (m == 26):
        break

    print(m)

for i in range(5):
    pass