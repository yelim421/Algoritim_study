n = int(input())

k = n
for i in range(n):
    for j in range(k):
        print('*', end = "")
    k -= 1
    print("")
