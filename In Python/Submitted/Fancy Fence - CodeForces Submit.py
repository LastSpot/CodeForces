numberTest = int(input())
test = 0
def polygonCheck(angle):
    x = 360/(180-angle)
    if x % 1 == 0:
        print('YES')
    else:
        print('NO')
while test != numberTest:
    angle = int(input())
    polygonCheck(angle)
    test += 1