# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            layer_val = []
            new_queue = []
            for node in queue:
                if node is not None:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                val = node.val if node is not None else None
                layer_val.append(val)
            if layer_val != layer_val[::-1]:
                return False
            queue = new_queue
        return True

# 递归解法
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def t_equal_rec(l,r):
            if not l and not r: return True
            if not l or not r: return False
            return l.val==r.val and t_equal_rec(l.left, r.right) and t_equal_rec(l.right, r.left)
        if not root: return True
        return t_equal_rec(root.left, root.right)