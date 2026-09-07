class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fs, ft = {}, {}
        for ch in s:
            fs[ch] = fs.get(ch, 0) + 1
        for ch in t:
            ft[ch] = ft.get(ch, 0) + 1
        if fs == ft:
            return True
        return False
