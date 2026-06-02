class Solution:
    def solve(self, bt):
        #your code goes here
        bt = sorted(bt)
        n = len(bt)
        s = 0
        o = 0
        for i in range(1,n):
            s = s+bt[i-1]
            o = o+s
        return o//n
        
