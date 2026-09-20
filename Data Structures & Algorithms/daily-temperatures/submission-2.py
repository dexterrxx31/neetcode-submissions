class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0

            stack.append(i)

        return result

        # for r, n in enumerate(temperatures):
        #     while stack and
        #         i = stack.pop()
        #         result[i] = r - i
        #     stack.append(r)
