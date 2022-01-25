a = list(input())
b = list(input())
c = list(input())
d = list(input())
def square(a,b,c,d):
    iq = 0
    for i in range(0,3):
        if a[i] == a[i+1] == b[i] or a[i] == a[i+1] == b[i+1]:
            iq += 1
        elif b[i] == b[i+1] == a[i] or b[i] == b[i+1] == a[i+1]:
            iq += 1
        elif b[i] == b[i+1] == c[i] or b[i] == b[i+1] == c[i+1]:
            iq = 1
        elif c[i] == c[i+1] == b[i] or c[i] == c[i+1] == b[i+1]:
            iq = 1
        elif c[i] == c[i+1] == d[i] or c[i] == c[i+1] == d[i+1]:
            iq = 1
        elif d[i] == d[i+1] == c[i] or d[i] == d[i+1] == c[i+1]:
            iq += 1
        else:
            iq += 0
    if iq > 0:
        print('YES')
    else:
        print('NO')
square(a,b,c,d)