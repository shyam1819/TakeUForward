class Solution:
    def maxSubArray(self, nums):
        current = 0
        maxSum = float("-inf")
        for i in range(len(nums)):
            current+=nums[i]
            if current>maxSum:
                maxSum = current
            if current<0:
                current = 0
        return maxSum
