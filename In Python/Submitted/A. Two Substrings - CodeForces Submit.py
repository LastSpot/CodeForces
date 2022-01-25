string = list(input())
stringVertwo = string.copy()
substring = []
substringVertwo = []
if len(string) > 3:
    for i in range(len(string)-1):
        if string[i] == 'A' and string[i+1] == 'B':
            x = string[i] + string[i+1]
            substring.append(x)
            string [i] = ''
            string [i+1] = ''
            break
    for n in range(len(string)-1):
        if string[n] == 'B' and string[n+1] == 'A':
            y = string[n] + string[n+1]
            substring.append(y)
            break
    if 'AB' in substring and 'BA' in substring:
        print('YES')
    elif len(stringVertwo) > 4:
        for j in range(len(stringVertwo)-1):
            if stringVertwo[j] == 'B' and stringVertwo[j+1] == 'A':
                a = stringVertwo[j] + stringVertwo[j+1]
                substringVertwo.append(a)
                string [j] = ''
                string [j+1] = ''
                break
        for k in range(len(stringVertwo)-1):
            if string[k] == 'A' and string[k+1] == 'B':
                b = string[k] + string[k+1]
                substringVertwo.append(b)
                break
        if 'AB' in substringVertwo and 'BA' in substringVertwo:
            print('YES')
        else:
            print('NO')
    else:
            print('NO')
else:
    print('NO')