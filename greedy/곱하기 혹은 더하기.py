s = int(input())
sum = 0

for i in map(int, str(s)):
    if i == 1 or 0:
        sum += i
    else:
        if sum == 0:
            sum = 1
        sum *= i
print(sum)