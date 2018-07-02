# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layer = [root]
        result = list()
        while layer:
            new_layer = list()
            layer_result = list()
            for note in layer:
                if note is None:
                    continue
                else:
                    new_layer.append(note.left)
                    new_layer.append(note.right)
                    layer_result.append(note.val)
            layer = new_layer
            if layer_result:
                result.append(layer_result)
        return result