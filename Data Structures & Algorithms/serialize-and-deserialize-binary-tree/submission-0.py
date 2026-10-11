# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        val = []

        def preorder(node):
            if not node:
                val.append("N")
                return

            val.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(val)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))

        def build():
            val = next(vals)

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()

            return node

        return build()
