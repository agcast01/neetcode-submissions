class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(len(nums)):
            if x == len(nums) - 1:
                return False
            if nums[x] == nums[x + 1]:
                return True
            continue
        return False