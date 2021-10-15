class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(com, remainder):
            if sum(com) == target :
                res.append(com)
                return 0
            elif sum(com)>target: return
            else:
                for i, value in enumerate(remainder):
                    dfs(com+[value], remainder[i:])
        res = []
        candidates.sort()
        dfs([], candidates)
        return res