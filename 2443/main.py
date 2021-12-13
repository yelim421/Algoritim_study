n = int(input())
k = n
a = 0
for i in range(n):
    for j in range(a):
            print(" ", end = "")
    a += 1
    for j in range(k):
        print("*", end = "")
    for j in range(k-1):
        print("*", end = "")
    k -= 1
    print("")