n = int(input())
maxA = int(n/1234567)
maxB = int(n/123456)
def check(n,maxA,maxB):
    for a in range(0,maxA+1):
        for b in range(0,maxB+1):
            target = n-(a*1234567)-(b*123456)
            if target >= 0 and target%1234 == 0:
                return 1
    return 2
if check(n,maxA,maxB) == 1:
    print('YES')
else:
    print('NO')