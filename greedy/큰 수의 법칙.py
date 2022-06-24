n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

sum = 0
count = 0 #제일 큰 수를 더한 횟수 카운터

while count < m:
    for i in range(k) :
        sum += data[0]
        count += 1
    sum += data[1]
    count += 1
    





print(sum)

#그럼 가장 큰 수 k번 을 더하고 두번째로 큰 수 1번을 더하는 걸 m번 반복하는거 아닐까?