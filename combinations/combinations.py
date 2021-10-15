class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if not n or not k:
            return 0
        
        def dfs(com, i, k):
           
            if k == 0:
                res.append(com[:])
                return 
            for j in range(i, n+1):
                com.append(j)
                dfs(com, j+1, k-1)
                com.pop()
        dfs([],1,k)
        return res