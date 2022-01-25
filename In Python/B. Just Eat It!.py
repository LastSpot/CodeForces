numberofTestcases = int(input())
for numberOftest in range(numberofTestcases):
    adelScore = 0
    adel = []
    n = int(input())
    tastiness = list(map(int, input().split()))
    yasser = sum(tastiness)
    for everything in range(len(tastiness)):
        adel.append(tastiness[everything])
    newAdel = sorted(adel, reverse = True)
    if yasser > newAdel[0]:
        if n > 2:
            for number in range(0,int(n)-1):
                tasteTest = tastiness[number] + tastiness[number+1]
                adel.append(tasteTest)
        for heads in range(1,len(tastiness)):
            keepCountone = 0
            for tails in range(heads,len(tastiness)):
                keepCountone += tastiness[tails]
                adel.append(keepCountone)
        for pets in range(0,len(tastiness)):
            keepCounttwo = 0
            for puppies in range(pets,len(tastiness)-1):
                keepCounttwo += tastiness[puppies]
                adel.append(keepCounttwo)
        newAdel = sorted(adel, reverse = True)
        if yasser > newAdel[0]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')