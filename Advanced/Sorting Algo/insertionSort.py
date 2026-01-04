class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1,n):
            index=i
            curr = nums.pop(i)
            for j in range(i-1,-1,-1):
                if nums[j]>curr:
                    index = j
            nums.insert(index,curr)
        return nums            
