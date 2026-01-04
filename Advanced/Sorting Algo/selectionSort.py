class Solution:
    def selectionSort(self, nums):
      """
      Constantly finds the smallest value in the unsorted array.
      """
        n = len(nums)
        for i in range(n):
            minIndex = i
            for j in range(i+1,n):
                if nums[j]<nums[minIndex]:
                    minIndex = j
            nums[i],nums[minIndex] = nums[minIndex],nums[i]
        return nums
