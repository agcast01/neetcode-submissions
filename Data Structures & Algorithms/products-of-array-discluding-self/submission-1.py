class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        for i in range(len(nums) - 1):
            output.append(nums[i] * output[i])
        
        postFix = 1
        for i in range(1, len(nums) + 1):
            output[-i] *= postFix
            postFix *= nums[-i]
        return output