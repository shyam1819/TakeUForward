class Solution:
    def searchMatrix(self, mat, target):
        searchIndex = self.searchInsert(mat,target)
        searchIndex = (searchIndex-1) if searchIndex!=0 else 0
        # print(searchIndex)
        return self.binarySearch(mat[searchIndex],target)

    def binarySearch(self,nums,target):
        n = len(nums)
        high = n-1
        low = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return False

    def searchInsert(self, nums, target):
        n = len(nums)
        high = n-1
        low = 0
        while low<=high:
            pivot = (low+high)//2
            if target == nums[pivot][0]:
                return pivot+1
            elif target > nums[pivot][0]:
                low = pivot+1
            else:
                high = pivot-1
        return pivot+1 if nums[pivot][0]<target else pivot
