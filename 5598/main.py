str = input()
dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''

for i in str:
    res += dic[dic.index(i)-3]

print(res)