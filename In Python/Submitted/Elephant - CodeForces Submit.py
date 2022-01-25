x = int(input())
moveNumber = 0
def move(x):
    if x%5 == 0:
        return int(x/5)
    else:
        return int(x/5) + 1
print(move(x))