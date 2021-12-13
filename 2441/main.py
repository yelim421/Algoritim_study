n = int(input())
k = n
l = 0

for i in range(n):
    for j in range(l):
        print(' ',  end = "")
    l += 1
    for j in range(k):
        print('*', end = "")
    k -= 1
    print("")