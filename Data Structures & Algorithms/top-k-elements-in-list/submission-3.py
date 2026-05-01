class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        buckets = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for key in count:
            buckets[count[key] - 1].append(key)
        print(buckets)
        res = []
        for r in reversed(buckets):
            print(r)
            if len(res) == k:
                return res
            if len(r) > 0:
                for n in r:
                    if len(res) == k:
                        return res
                    res.append(n)
        return res
    
        