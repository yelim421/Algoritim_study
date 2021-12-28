T = int(input())

for i in range(T):
    str = input().split()
    print(str)
    res = list()
    for i in range(len(str)):
        string = str[i]
        res = "".join(reversed(string))
            
        print(res, end = ' ')