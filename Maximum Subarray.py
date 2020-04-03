class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        # 6 -> [4,-1,2,1]

        val = nums[0]
        maxVal = val

        for i in range(1, len(nums)):
            temp = nums[i]

            if val <= 0 and temp > 0:
                val = temp
            else:
                val += temp

            maxVal = max(maxVal, val, temp)

        return maxVal
                
