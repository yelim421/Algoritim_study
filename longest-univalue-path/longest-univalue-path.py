# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result : int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root.left and root.left.val == root.val:
                left += 1
            else: left = 0
            
            if root.right and root.right.val == root.val:
                right += 1
            else: right = 0
            
            self.result = max(self.result, left+right)
            return max(left, right)
        dfs(root)
        return self.result