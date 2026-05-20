class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            count = [0] * 26
            for char in word: 
                index = ord(char) - ord('a')
                count[index] += 1

            signature = tuple(count)

            if signature not in anagram_map:
                anagram_map[signature] = [word]
            else:
                anagram_map[signature].append(word)

        return list(anagram_map.values())