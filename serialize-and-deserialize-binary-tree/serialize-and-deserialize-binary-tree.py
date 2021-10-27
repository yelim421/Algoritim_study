# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        if not root: return 'null,'
        left_serialize = self.serialize(root.left)
        right_serialize = self.serialize(root.right)
        return str(root.val)+','+left_serialize+right_serialize

    def deserialize(self, data):
        def dfs(queue):
            val = queue.popleft()
            if val == 'null': return None
            node = TreeNode(val)
            node.left = dfs(queue)
            node.right = dfs(queue)
            return node
        
        queue = deque(data.split(','))
        return dfs(queue)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))