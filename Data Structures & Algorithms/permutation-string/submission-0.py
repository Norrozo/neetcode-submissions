class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # dictionary counting
        s1_count = {}
        window_count = {}
        # for sliding window
        left = 0

        # count the characters in s1, if don't exist, place a zero and then add 1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        for right in range(len(s2)):

            # add tally to window count
            char = s2[right]
            window_count[char] = window_count.get(char, 0) + 1

            if (right - left + 1) > len(s1):
                left_char = s2[left]
                window_count[left_char] -= 1

                #if this character is seen from nowhere just remove it and delete it
                if window_count[left_char] == 0:
                    del window_count[left_char]

                left += 1
            
            if window_count == s1_count:
                return True

        return False
        