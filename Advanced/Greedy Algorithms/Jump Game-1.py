class Solution:
    def canJump(self, nums):
        #your code goes here
        n = len(nums)
        maxIndex = 0
        for i in range(n):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex,i+nums[i])
        
        return True
