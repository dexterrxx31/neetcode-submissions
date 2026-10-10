# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.rec(root, root.val)

    def rec(self, node, max_v):
        if not node:
            return 0
        curr = 1 if node.val >= max_v else 0
        max_v = max(node.val, max_v)
        return curr + self.rec(node.left, max_v) + self.rec(node.right, max_v)
