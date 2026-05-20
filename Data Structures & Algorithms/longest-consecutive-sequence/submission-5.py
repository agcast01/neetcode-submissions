class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxStreak = 1
        if len(nums) == 0:
            return 0
        numSet = set()
        for num in nums:
            numSet.add(num)
        i = 0
        while i < len(nums):
            j = 1
            while nums[i] + j in numSet:
                if j + 1 > maxStreak:
                    maxStreak = j + 1
                j += 1
            i += 1

        return maxStreak