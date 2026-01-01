class Solution:
    def isomorphicString(self, s, t):
        # Arrays to store the last seen positions of characters in s and t
        m1, m2 = [0] * 256, [0] * 256
        
        # Length of the string
        n = len(s)
        
        # Iterate through each character in the strings
        for i in range(n):
            # If the last seen positions of the current characters don't match, return false
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            
            # Update the last seen positions
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        
        # If all characters match, return true
        return True
