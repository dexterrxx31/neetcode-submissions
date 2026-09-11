class Solution:
    def encode(self, strs: List[str]) -> str:
        r = []
        for s in strs:
            r.append(str(len(s)) + "#" + s)
        return "".join(r)

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            start = j + 1
            end = l + start
            r.append(s[start:end])
            i = end
        return r
