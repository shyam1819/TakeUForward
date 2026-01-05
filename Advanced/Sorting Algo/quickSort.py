class Solution:
    def setPivot(self,nums,low,high):
        pivot = low
        i=low
        j=high
        while i<j:
            while nums[i]<=nums[pivot] and i<high:
                i+=1
            while nums[j]>=nums[pivot] and j>low:
                j-=1
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[pivot],nums[j] = nums[j], nums[pivot]
        return j
    def quickSortHelper(self,nums,low,high):
        if low>=high:
            return
        pIndex = self.setPivot(nums,low,high)
        self.quickSortHelper(nums,low,pIndex-1)
        self.quickSortHelper(nums,pIndex+1,high)
    def quickSort(self, nums):
        low =0
        high = len(nums)-1
        self.quickSortHelper(nums,low,high)
        return nums
