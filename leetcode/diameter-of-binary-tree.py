# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTreeSub(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0, 0
        left_diameter = 0
        left_depth = 0
        right_diameter = 0
        right_depth = 0
        if root.left:
            left_diameter, left_depth = self.diameterOfBinaryTreeSub(root.left)
            left_depth += 1
        if root.right:
            right_diameter, right_depth = self.diameterOfBinaryTreeSub(root.right)
            right_depth += 1

        max_diameter = max(left_diameter,right_diameter, left_depth + right_depth)
        max_depth = max(left_depth, right_depth)
        return max_diameter, max_depth

    def diameterOfBinaryTree(self, root):
        max_diameter, max_depth = self.diameterOfBinaryTreeSub(root)
        return max_diameter


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        helper(root)
        return self.res