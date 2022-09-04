n, m = map(int, input().split()) #N*M
data = [list(map(int,input().split())) for _ in range(n)]
ans = []

print(data)

for i in data:
    ans.append(min(i))
    
print(max(ans))