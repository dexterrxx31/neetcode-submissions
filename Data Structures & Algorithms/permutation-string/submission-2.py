class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        mp_s1, mp_s2 = {}, {}

        for x in s1:
            mp_s1[x] = mp_s1.get(x, 0) + 1

        for x in range(l1):
            mp_s2[s2[x]] = mp_s2.get(s2[x], 0) + 1

        if mp_s1 == mp_s2:
            return True

        for c in range(l1, l2):
            mp_s2[s2[c]] = mp_s2.get(s2[c], 0) + 1
            mp_s2[s2[c - l1]] -= 1

            if mp_s2.get(s2[c - l1]) == 0:
                del mp_s2[s2[c - l1]]

            if mp_s2 == mp_s1:
                return True

        return False
