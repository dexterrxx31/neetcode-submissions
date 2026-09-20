class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for r, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                i = stack.pop()
                result[i] = r - i
            stack.append(r)

        return result