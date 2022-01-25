testCases = int(input())
def sweetDays(testCases):
    case = 0
    while case != testCases:
        rgb = list(map(int, input().split()))
        case += 1
        x = sum(rgb)
        if x % 2 == 0 and rgb[0] % 2 == 0 and rgb[1] % 2 == 0 and rgb[2] % 2 == 0:
            print(int(x/2))
        else:
            a = sorted(rgb,reverse = True)
            b = a[0] - a[1]
            if b >= a[2]:
                print(int(a[1] + a[2]))
            else:
                print(int(a[1] + b))
sweetDays(testCases)