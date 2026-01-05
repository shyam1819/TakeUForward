class Solution:
    def merge(self,arr,low,mid,high):
        temp = []
        left = low
        right = mid+1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i] = temp[i-low]

    def mergeSortHelper(self,arr,low,high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeSortHelper(arr,low,mid)
        self.mergeSortHelper(arr,mid+1,high)
        self.merge(arr,low,mid,high)
        
    def mergeSort(self, nums):
        low = 0
        high = len(nums)-1
        self.mergeSortHelper(nums,low,high)
        return nums
        

print(sorter.mergeSort([7,4,1,5,3]))
