numberTest = int(input())
testDone = 0
def array(numberTest):
    lengthArray = int(input())
    test = list(map(int, input().split()))
    x = sorted(test, reverse = True)
    listToStr = ' '.join([str(elem) for elem in x]) 
    print(listToStr)
while testDone < numberTest:
    array(numberTest)
    testDone += 1