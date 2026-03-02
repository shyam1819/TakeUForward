class Solution:
    """Function to check if it's possible to make
    m bouquets with k flowers each on a given day"""
    def possible(self, nums, day, m, k):
        n = len(nums)
        
        # Count of flowers bloomed
        cnt = 0 
        
        # Count of bouquets formed
        noOfB = 0 

        # Count number of bouquets that can be formed
        for i in range(n):
            if nums[i] <= day:
                # Increment flower count
                cnt += 1 
            else:
                # Calculate number of bouquets formed with flowers <= day
                noOfB += (cnt // k)
                
                # Reset flower count
                cnt = 0 
        
        # Add remaining flowers as a bouquet
        noOfB += (cnt // k) 
        
        # Return true if enough bouquets can be formed
        return noOfB

    """Function to find the earliest day to
    make m bouquets of k flowers each"""
    def roseGarden(self, n, nums, k, m):
        # Calculate the minimum number of flowers required
        val = m * k 
        
        # Impossible case: not enough flowers to make m bouquets
        if val > n:
            return -1 
        
        # Find maximum and minimum bloom days in the array
        mini = float('inf')
        maxi = float('-inf')
        for num in nums:
            mini = min(mini, num) 
            maxi = max(maxi, num) 
        
        # Linear search to find the earliest day to make m bouquets
        minDays = -1
        # for i in range(mini, maxi + 1):
        #     if self.possible(nums, i, m, k):
        #         return i
        while mini<=maxi:
            mid = (mini+maxi)//2
            if self.possible(nums,mid,m,k)>=m:
                maxi = mid-1
                minDays = mid
            else:
                mini = mid+1

        # Return -1 if no such day exists
        return minDays
