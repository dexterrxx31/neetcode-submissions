# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.ans = 0

        self.rec(root, k)
        return self.ans

    def rec(self, node, k):
        if not node or self.count >= k:
            return

        self.rec(node.left, k)

        if self.count >= k:
            return

        self.count += 1

        if self.count == k:
            self.ans = node.val
            return

        self.rec(node.right, k)
