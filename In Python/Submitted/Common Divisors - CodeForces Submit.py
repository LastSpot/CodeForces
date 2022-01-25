n = int(input())
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
a = list(map(int, input().split()))

result = a[0]

for i in a[1:]:
    result = gcd(result, i)

def printDivisors(result):
    count = 0
    countList = []
    i = 1
    while i <= (result)**(1/2) : 
        if (result % i==0 and i != (result)**(1/2)): 
            count+=2
        elif (i==(result)**(1/2)):
            count+=1
        i+=1
    print(count)
printDivisors(result)