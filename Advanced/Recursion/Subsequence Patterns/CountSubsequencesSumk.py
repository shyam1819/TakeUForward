class Solution:

    def _recursive_subsequence(self,i,n,nums,k,ans):
        # Termination condition
        if k==0:
            ans+=1
            return ans
        if k<0:
            return ans
        if i==n:
            if k==0:
                ans+=1
            return ans
        # Covering two case 1. Including the subsequence with the current index and 2. Without current index
        # Exhausting all possible cases.
        return self._recursive_subsequence(i+1,n,nums,k-nums[i],ans) + self._recursive_subsequence(i+1,n,nums,k,ans)


    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        n = len(nums)

        ans = self._recursive_subsequence(0,n,nums,k,0)
        return ans
