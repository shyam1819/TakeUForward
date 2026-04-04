class Solution:
    def longestOnes(self, nums, k):
        #your code goes here
        zeros = 0
        left = 0
        maxLen = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            maxLen = max(right-left+1,maxLen)
        return maxLen
