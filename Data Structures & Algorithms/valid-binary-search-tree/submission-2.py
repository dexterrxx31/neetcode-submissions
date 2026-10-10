# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.rec(root, float("inf"), float("-inf"))
        else:
            return True

    def rec(self, root, max_v, min_v):
        if not root:
            return True

        if root.val >= max_v or root.val <= min_v:
            return False

        left_bool = self.rec(root.left, root.val, min_v)
        right_bool = self.rec(root.right, max_v, root.val)

        return left_bool and right_bool
