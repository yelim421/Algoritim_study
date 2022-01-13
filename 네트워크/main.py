def solution(n, computers):
    answer = 0
    dic = {}
    for i, num in enumerate(computers):
        dic[i] = computers[i]#[j for j in range(n) if computers[j]==num]
    
    for i in range(max(dic)):
        if i == dic[i][i]:
            del (dic[i][i])
        
    print(dic)
    #print(dic[1][1])
    
    def dfs(start, visited = []):
        #visited = []
        visited.append(start)
        for i in dic[start]:
            if not i in visited:
                visited = dfs(i, visited)
        return visited
    
    answer = len(dfs(1))
    
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	)) #2

#[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#{0: [1], 1: [0], 2: [2]}