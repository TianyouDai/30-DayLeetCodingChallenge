class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        res = []

        for i in nums:
            if i not in res:
                res.append(i)
            else:
                res.remove(i)
        return res[0]
        
