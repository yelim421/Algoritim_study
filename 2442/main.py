n = int(input())
k = n-1
a = 1
for i in range(n):
    for j in range(k):
        print(" ", end = "")
    k -= 1
    for j in range(a):
        print("*", end = "")
    for j in range(a-1):
            print("*", end = "")
    a += 1
    print("")