#뭐 보고했음
def solution(priorities, location):
    answer = 0
    dic = {}
    
    for i, order in enumerate(priorities):
        dic[i] = order
    
    while priorities[location] > 0:
        for i in dic:
            if dic[i] == max(dic.values()):
                answer += 1
                
                if i == location :
                    return answer
                dic[i] = 0

print(solution([1, 1, 9, 1, 1, 1], 0))