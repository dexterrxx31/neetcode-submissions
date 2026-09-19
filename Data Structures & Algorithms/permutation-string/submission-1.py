class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mp_s1, mp_s2 = {}, {}
        l = len(s1)

        for x in s1:
            mp_s1[x] = mp_s1.get(x, 0) + 1

        for x in range(l):
            mp_s2[s2[x]] = mp_s2.get(s2[x], 0) + 1

        if mp_s1 == mp_s2:
            return True

        for c in range(l, len(s2)):
            mp_s2[s2[c]] = mp_s2.get(s2[c], 0) + 1
            mp_s2[s2[c - l]] -= 1

            if mp_s2.get(s2[c - l]) == 0:
                del mp_s2[s2[c - l]]

            if mp_s2 == mp_s1:
                return True

        return False
