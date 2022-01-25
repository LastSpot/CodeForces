n = list(map(int, input().split()))
x = list(map(int, input().split()))
count = 0
for i in range(n[0]):
    if x[i] >= x[n[1] - 1] and x[i] > 0:
        count += 1
print(count)