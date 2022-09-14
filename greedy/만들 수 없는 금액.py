from itertools import combinations

n = int(input())
s = list(map(int,input().split()))
s.sort()

source = []
source.extend(s)
for j in range(n):  
    for i in list(combinations(s, j+1)):
        source.append(sum(i))
ans = set(source) 
ans = list(ans)

range_list=list(range(1, ans[-1]+1))

for i in range(1,ans[-1]):
    if i not in ans:
        print(i)
        break
if ans==range_list:
    print(ans[-1]+1)