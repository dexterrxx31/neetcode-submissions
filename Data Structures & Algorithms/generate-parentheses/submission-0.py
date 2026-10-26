class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, path = [], []
        open, close = 0, 0

        def bt(o, c):
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if o < n:
                path.append("(")
                bt(o + 1, c)
                path.pop()
            if c < o:
                path.append(")")
                bt(o, c + 1)
                path.pop()

        bt(0, 0)
        return result
