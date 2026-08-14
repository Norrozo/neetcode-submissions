class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # length of the loop
        output = [1] * n # creates the output array

        prefix = 1 # to the left of the value
        for i in range(n):
            output[i] = prefix #record number
            prefix *= nums[i] #record prefix values

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix = nums[i] * suffix
    
        return output