num = int(input())
for i in range(num):
    string = str(input())
    if len(string) > 10:
        n = len(string) - 2
        print(string[0], n, string[len(string) - 1], sep= "")
    else:
        print(string)