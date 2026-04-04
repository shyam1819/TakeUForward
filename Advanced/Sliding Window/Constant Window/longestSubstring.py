class Solution:
    def longestNonRepeatingSubstring(self, s):
        #your code goes here
        n = len(s)
        lookup = set()
        maxLen = 0
        count = 0
        i,j = 0,0
        while j<n:
            if s[j] not in lookup:
                lookup.add(s[j])
                count+=1
                j+=1
            else:
                while s[i]!=s[j]:
                    lookup.discard(s[i])
                    i+=1
                    count-=1
                i+=1
                j+=1
            maxLen = max(count,maxLen)

        return maxLen
