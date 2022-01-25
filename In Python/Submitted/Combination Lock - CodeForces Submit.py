disks = int(input())
x = str(input())
y = str(input())
move = 0
def unlock(x,y,move):
    for i in range(len(x)):
        if x[i] > y[i]:
            if int(x[i]) - int(y[i]) > 5:
                move += (10 - (int(x[i]) - int(y[i])))
            else:
                move += (int(x[i]) - int(y[i]))
        else:
            if int(y[i]) - int(x[i]) > 5:
                move += (10 - (int(y[i]) - int(x[i])))
            else:
                move += (int(y[i]) - int(x[i]))
    print(move)

unlock(x,y,move)