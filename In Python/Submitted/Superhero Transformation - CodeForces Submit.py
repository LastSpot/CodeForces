x = list(input())
y = list(input())
vowel = ['a','e','i','o','u']
cosonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
def hero(x,y):
    numberFalse = 0
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] in vowel and y[i] in vowel:
                numberFalse += 0
            elif x[i] in cosonant and y[i] in cosonant:
                numberFalse += 0
            else:
                numberFalse += 1
    else:
        numberFalse += 1
    if numberFalse > 0:
        print('NO')
    else:
        print('YES')
hero(x,y)