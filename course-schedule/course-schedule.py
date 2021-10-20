class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(x):
            if x in traced:
                return False
            if x in visited:
                return True
            
            traced.add(x)
            for y in graph[x]:
                if not dfs(y):
                    return False
            traced.remove(x)
            
            visited.add(x)
            return True
        
        
        graph = collections.defaultdict(list)
        
        for x,y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        for x in list(graph):
            print(x)
            if not dfs(x):
                return False
        return True
    
        