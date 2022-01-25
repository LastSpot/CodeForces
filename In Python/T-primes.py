n = int(input())
x = list(map(int, input().split()))
def divisor(number):
    divide = []
    for a in range(2, (int(number)^(1/2)) + 1):
        if number % a == 0:
            divide.append(a)
    if len(divide) == 1:
        print('YES')
    else:
        print('NO')
for i in range(n):
    divisor(x[i])