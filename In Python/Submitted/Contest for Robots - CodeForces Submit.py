def score(a,b,n):
    aSolve = 0
    bSolve = 0
    impossible = 0
    for i in range(0,n):
        if a[i] > b[i]:
            aSolve += 1
        elif a[i] < b[i]:
            bSolve += 1
        else:
            impossible += 1
    if impossible == n:
        print(-1)
    elif aSolve == 0 and bSolve > 0:
        print(-1)
    else:
        if aSolve > bSolve:
            print(1)
        else:
            x = bSolve + 1
            y = x/aSolve
            if y%1 == 0:
                print(int(y))
            else:
                print(int(y)+1)
 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
score(a,b,n)