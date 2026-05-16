class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        needed = {}
        for index, value in enumerate(nums):
            difference = target - value

            if difference in needed: 
                return[needed[difference], index]

            needed[value] = index