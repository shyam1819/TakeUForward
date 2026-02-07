class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)
        pos = self.searchInsert(nums,x)
        if pos==n:
            return [nums[pos-1],-1]
        elif nums[pos]==x:
            return [x,x]
        elif pos==0:
            return [-1,nums[pos]]
        else:
            return [nums[pos-1],nums[pos]]
        
    def searchInsert(self, nums, target):
        n = len(nums)
        high = n-1
        low = 0
        while low<=high:
            pivot = (low+high)//2
            if target == nums[pivot]:
                return pivot
            elif target > nums[pivot]:
                low = pivot+1
            else:
                high = pivot-1
        return low
