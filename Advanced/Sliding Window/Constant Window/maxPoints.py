class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        maxSum = float("-inf")
        curr = sum(cardScore[0:k])
        i=0
        j=k-1
        while j>=-1:
            maxSum = max(maxSum,curr)
            i-=1
            curr = curr-cardScore[j]+cardScore[i]
            j-=1
        return maxSum

