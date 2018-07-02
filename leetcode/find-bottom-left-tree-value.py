# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n, v = self.helper(root)
        return v

    def helper(self, root):
        if root is None:
            return 0, None

        nl, vl = self.helper(root.left)
        nr, vr = self.helper(root.right)
        if nl == 0 and nr == 0:
            return 1, root.val
        elif nl >= nr:
            return nl + 1, vl
        else:
            return nr + 1, vr


# 非递归，逐层遍历
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        res = []
        while len(queue) > 0:
            res.append([q.val for q in queue])
            temp_queue = []
            for q in queue:
                if q.left:
                    temp_queue.append(q.left)
                if q.right:
                    temp_queue.append(q.right)
            queue = temp_queue

        return res[-1][0]

# 看着应该很快但实际并不比我的快
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        a = [root]

        while a:
            root = a.pop(0)
            if root.right != None:
                a.append(root.right)
            if root.left != None:
                a.append(root.left)
        return root.val
