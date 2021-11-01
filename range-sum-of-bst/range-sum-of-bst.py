# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        tree = [root]
        sum = 0
        while tree :
            node = tree.pop()
            if node : 
                if node.val > low : tree.append(node.left)
                if node.val < high : tree.append(node.right)
                if low <= node.val <= high : sum += node.val
        return sum