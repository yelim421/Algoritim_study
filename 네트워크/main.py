from shlex import join


def solution(n, computers):
    answer = 0
    dic = {}
    new_dic = {}
    for i, num in enumerate(computers):
        dic[i] = computers[i]#[j for j in range(n) if computers[j]==num]
    
    print(max(dic))
    
    for i in range(max(dic)+1):
        for j in range(max(dic)+1):
            if dic[i][j] == 1:
                dic[i][j] = j
            elif dic[i][j] == 0:
                dic[i][j] = 0
    print(dic)
    
    for i in range(max(dic)):
        if dic[i][i] == 1:
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
    
    answer = len(dfs(0))
    
    return answer


print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])) #2

#[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#{0: [1], 1: [0], 2: [2]}