class Solution:
    def twoSum(self, nums, target):
        diffMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            index = diffMap.get(nums[i],None)
            if index is None:
                diffMap[diff] = i
            else:
                return [index,i]
        return [-1,-1]        
