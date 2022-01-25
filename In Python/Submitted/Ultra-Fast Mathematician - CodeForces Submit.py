x = list(input())
y = list(input())
for i in range(len(x)):
    if x[i] > y[i] or x[i] < y[i]:
        x[i] = 1
    else:
        x[i] = 0
for i in x: 
    print(i, end="") 