class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        stack = []

        for e in tokens:
            if e in ops:
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(ops[e](e2, e1))
            else:
                stack.append(int(e))

        return stack[0]
