class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        maxStreak = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            num = nums[i]
            if nums[i] == nums[i - 1] + 1:
                count += 1
                if count > maxStreak:
                    maxStreak = count
            elif nums[i] == nums[i - 1]:
                continue
            else:
                if count > maxStreak:
                    maxStreak = count
                count = 1
        return maxStreak