class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = Counter(t)  # dict of t
        have = 0  # no of character satisfied
        required = len(need)  # required character to satisfy

        window = {}
        l = 0
        lf, rf = 0, -1
        best = float("inf")

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:  # condition to satisfy char need
                have += 1

            while have == required:  # Bingo we got matching window
                if r - l + 1 < best:
                    best = r - l + 1
                    lf, rf = l, r
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return s[lf : rf + 1] if best < float("inf") else ""
