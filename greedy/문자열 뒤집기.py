s = input()
j = -1
count = 0
a = s[0]
tem = s[j]


for i in s:
    tem = s[j]
    if tem == a:
        if i != a:
            count += 1
    j += 1

print(count)
