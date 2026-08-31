class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        countT = {}
        window = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        have = 0
        need = len(countT)

        #this is result, we set it arb. and wait until optimal length comes
        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        # add the right character into the window dictionary
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            #gate to make sure the min requirements are satisfied
            if char in countT and window[char] == countT[char]:
                have += 1

            #looks at all the valid combinations
            while have == need:
        
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)

                # update so that left is decreasing in size
                left_char = s[left]
                window[left_char] -= 1
                
                #count down the have so that it removes
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                #update so that left is going smaller
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""