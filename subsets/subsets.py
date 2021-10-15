

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    def dfs(self,nums, index, element, res):
        res.append(element)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, element+[nums[i]], res)