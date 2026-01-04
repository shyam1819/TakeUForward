class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        while True:
            swapped = False
            for i in range(0,n-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
                    swapped = True
            if swapped == False:
                break
        return nums
