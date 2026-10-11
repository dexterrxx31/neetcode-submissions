# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self.maxGain(root)
        return self.max_sum

    def maxGain(self, node):
        if not node:
            return 0

        left = max(0, self.maxGain(node.left))
        right = max(0, self.maxGain(node.right))

        current_path_sum = left + node.val + right

        self.max_sum = max(self.max_sum, current_path_sum)

        return node.val + max(left, right)
