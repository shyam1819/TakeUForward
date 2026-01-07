class Solution:
    def leaders(self, nums):
        n = len(nums)
        maximum = float("-inf")
        leaders = []
        for i in range(n-1,-1,-1):
            if nums[i]>maximum:
                leaders.insert(0,nums[i])
                maximum = nums[i]
        return leaders
