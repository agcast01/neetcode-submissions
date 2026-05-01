class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = set()
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict.add(num)
        return False