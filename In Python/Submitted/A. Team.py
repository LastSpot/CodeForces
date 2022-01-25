num = int(input())
n = 0
for i in range(num):
    count = 0
    a = list(map(int, input().split()))
    if (a[0] == 1 or a[1] == 1 or a[2] == 1):
        count += 1
print(n)