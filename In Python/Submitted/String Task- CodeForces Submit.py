word = str(input())
lower = word.lower()
newWord = list(lower)
newWord = [string.replace('a', '') for string in newWord]
newWord = [string.replace('o', '') for string in newWord]
newWord = [string.replace('y', '') for string in newWord]
newWord = [string.replace('e', '') for string in newWord]
newWord = [string.replace('u', '') for string in newWord]
newWord = [string.replace('i', '') for string in newWord]
for i in range(len(newWord)):
    if newWord[i] != "":
        newWord[i] = '.' + newWord[i]
result ="".join(newWord)
print(result)