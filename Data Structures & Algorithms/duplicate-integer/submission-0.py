class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                return True
        return False
