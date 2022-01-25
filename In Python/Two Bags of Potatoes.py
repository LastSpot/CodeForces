n = list(map(int, input().split()))
numbers = []
if n[0] == n[2]:
    print(-1)
else:
    for i in range(1,n[2]+1):
        x = n[0] + i
        value = x/n[1]
        if value % 1 == 0 and x < n[2]+1:
            numbers.append(i)
result = list(set(numbers))
print(*result)