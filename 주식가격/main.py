def solution(prices):
    answer = []
    dict = {}
    for i, order in enumerate(prices):
        dict[i] = order
    for i in dict:
        a = 0
        j = i+1
        while dict[i] <= dict[j]:
            a += 1
            j += 1
            if j == len(prices): 
                #answer.append(a)
                break
        answer.append(a)
    
    
    return answer

solution([1,2,3,2,3])