class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [], []

        def bt(start):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                substring = s[start : end + 1]

                if substring != substring[::-1]:
                    continue

                path.append(substring)
                bt(end + 1)
                path.pop()

        bt(0)
        return result
