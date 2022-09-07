N = int(input())
group = list(map(int,input().split()))
count = 0

group.sort()

while group:
    t = group[-1]
    group = group[:-t]
    count += 1

print(count)