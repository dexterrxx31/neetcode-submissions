class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l % 2 == 1:
            return False

        stack = []

        for ch in s:
            if stack and stack[-1] == {"]": "[", "}": "{", ")": "("}.get(ch):
                stack.pop()
            else:
                stack.append(ch)

        if not stack:
            return True
        else:
            return False
