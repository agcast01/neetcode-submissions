class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = 0

        for i in range(1, len(nums)):
            rSum += nums[i]

        for i in range(len(nums)):
            print(lSum, " : ", rSum)
            if i == len(nums) - 1:
                rSum = 0
                if lSum == rSum:
                    return i
                else:
                    return -1
            if lSum == rSum:
                return i
            lSum += nums[i]
            rSum -= nums[i + 1]