from itertools import combinations

n,m = map(int, input().split())
s = list(map(int,input().split()))

combi = list(combinations(s, 2))
res = len(combi)

# #중복 없애기
# new_s = list(set(s))
# res = res-len(s)+len(new_s)
# print(res)


for i in combi:  
   A, B = i  
   if A == B:  
       res -= 1  
print(res)