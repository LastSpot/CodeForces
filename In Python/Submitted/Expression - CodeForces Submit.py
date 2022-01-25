a = int(input())
b = int(input())
c = int(input())
answer = []
caseOne = a + b * c
answer.append(caseOne)
caseTwo = a * (b + c)
answer.append(caseTwo)
caseThree = a * b * c
answer.append(caseThree)
caseFour = (a + b) * c
answer.append(caseFour)
caseFive = a + b + c
answer.append(caseFive)
answerSorted = sorted(answer)
print(answerSorted[4])