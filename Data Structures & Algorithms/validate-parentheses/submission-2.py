class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)
        if l % 2 == 1:
            return False

        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
            elif stack[-1] == "[" and ch == "]":
                stack.pop()
            elif stack[-1] == "{" and ch == "}":
                stack.pop()
            elif stack[-1] == "(" and ch == ")":
                stack.pop()
            else:
                stack.append(ch)

        if not stack:
            return True
        else:
            return False
