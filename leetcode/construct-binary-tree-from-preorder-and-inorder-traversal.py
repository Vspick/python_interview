# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        print("---------")
        print("input preorder is %s" % preorder)
        print("input inorder is %s" % inorder)

        val = preorder[0]
        root = TreeNode(val)
        in_loc = inorder.index(val)
        print("in loc: %s" % in_loc)
        root.left = self.buildTree(preorder[1: in_loc + 1], inorder[0: in_loc])
        root.right = self.buildTree(preorder[in_loc + 1:], inorder[in_loc + 1:])
        return root


if __name__ == "__main__":
    obj = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    obj.buildTree(preorder, inorder)
