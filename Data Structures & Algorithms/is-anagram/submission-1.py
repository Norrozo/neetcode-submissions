class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        for l in s:
            if l not in count_s:
                count_s[l] = 1
            else:
                count_s[l] = count_s[l] + 1
        for l in t:
            if l not in count_t:
                count_t[l] = 1
            else:
                count_t[l] = count_t[l] + 1

        return count_s == count_t
    
