numberTrials = int(input())
numbers = list(input().split())
evenValues = []
oddValues = []
for i in range(numberTrials):
    evenChecking = int(numbers[i])/2
    if evenChecking % 1 == 0:
        evenValues.append(numbers[i])
    else:
        oddValues.append(numbers[i])

if len(evenValues) < len(oddValues):
    for n in range(len(numbers)):
        if evenValues[0] == numbers[n]:
            print(n+1)
else:
    for n in range(len(numbers)):
        if oddValues[0] == numbers[n]:
            print(n+1)