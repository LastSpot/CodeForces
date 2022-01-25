n = list(map(int, input().split()))
count = 0
for x in range(1, n[0] + 1):
    for y in range(1, n[1] + 1):
        a = x + y
        if a % 5 == 0:
            count += 1
print(count)