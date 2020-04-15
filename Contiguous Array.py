class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		res = 0
		tem = {0: -1}
		count = 0
		length = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				count += 1
			if nums[i] == 1:
				count -= 1
			if count in tem:
				length = i - tem[count]
			if count not in tem:
				tem[count] = i
			res = max(res,length)
		return res
