class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        path = []

        def bt(index):
            if index == len(digits):
                result.append("".join(path))
                return

            for letter in phone[digits[index]]:
                path.append(letter)
                bt(index + 1)
                path.pop()

        bt(0)
        return result
