a = int(input())
b = int(input())
c = a + b
x = str(a)
y = str(b)
z = str(c)
def zeroEraser(x,y,z):
    newA = x.replace('0','')
    newB = y.replace('0','')
    newC = z.replace('0','')
    resultCompare = int(newA) + int(newB)
    if resultCompare == int(newC):
        print('YES')
    else:
        print('NO')
zeroEraser(x,y,z)