n = list(map(int, input().split()))
even = []
odd = []
for i in range(1, int(n[0])+1):
    if (i/2) % 1 == 0:
        even.append(i)
    else:
        odd.append(i)
result = odd + even
print(result[n[1]-1])