def roll():
    x = int(input())
    print(int(x/2))
def rollTime(targetSet):
    targetInitial = 0
    while targetInitial < targetSet:
        roll()
        targetInitial += 1
targetSet = int(input())
rollTime(targetSet)