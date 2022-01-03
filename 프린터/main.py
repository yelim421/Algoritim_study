def solution(priorities, location):
    order = []
    priorities_first = priorities.copy()
    
    #for i in range(len(priorities)):
    while len(priorities)>0:
        if max(priorities) == priorities[0]:
            order.append(priorities[0])
            priorities.pop(0)
        #elif len(priorities) == 0 :
        #    break
        else :
            priorities.append(priorities.pop(0))
    print(order)
    answer = order.index(priorities_first[location])
    
    return answer+1

print(solution([1, 1, 9, 1, 1, 1], 0))