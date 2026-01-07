class Solution:
    def majorityElement(self, nums):
        candidate = -1
        votes = 0
        for i in nums:
            if votes == 0:
                candidate = i
                votes+=1
            else:
                if i == candidate:
                    votes+=1
                else:
                    votes-=1
        return candidate
