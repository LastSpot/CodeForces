n = int(input())
a = list(map(int, input().split()))
x = sorted(a)
y = x[len(x)-1]
print(y)