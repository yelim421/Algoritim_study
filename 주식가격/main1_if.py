#if문 사용해서...재시도 했음

def solution(prices):
    answer = []
    leng = len(prices)
    dict = {}
    for i, order in enumerate(prices):
        dict[i] = order
    for i in dict:
        a = 0
        for j in range(i+1,leng,1):
            if dict[i] > dict[j]:
                answer.append(j-i)
                break
            elif j == leng-1:
                answer.append(leng-i-1)
                break
    answer.append(0)
    return answer

print(solution([1,2,3,2,3]))