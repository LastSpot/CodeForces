n = int(input())
x = [int(x) for x in str(n)] 
for i in range(len(x)):
    if x[i] == 0:
        del x[i]
        break
else:
    del x[0]
result = int("".join(map(str, x)))
print(result)