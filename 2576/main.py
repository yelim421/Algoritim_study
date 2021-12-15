a = [0 for i in range(7)]
for i in range(7):
    a[i] = int(input())
    
res = []
for i in a:
    if (i%2 == 1) :
        res.append(i)
if len(res) == 0 : print("-1")
else : 
    print(sum(res))
    print(min(res))