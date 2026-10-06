# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return bool(self.rec(root, subRoot))

    def rec(self, root, subroot):
        if not subroot:
            return 1
        if not root:
            return 0

        if self.sameTree(root, subroot):
            return 1

        return self.rec(root.left, subroot) or self.rec(root.right, subroot)

    def sameTree(self, p, q):
        if not p and not q:
            return 1

        if not p or not q:
            return 0

        if p.val != q.val:
            return 0

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
