# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        
        depth = 0
        Q = deque([root])
        while Q:
            depth += 1
            for _ in range(len(Q)):
                current = Q.popleft()
                if current.left:
                    Q.append(current.left)
                if current.right:
                    Q.append(current.right)
        return depth 