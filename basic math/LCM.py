class Solution:
    def LCM(self, n1, n2):
        return (n1*n2)//self.GCD(n1,n2)

    def GCD(self,n1,n2):
        if n2>n1:
            n1,n2 = n2,n1
        while n2:
            n1, n2 = n2, n1%n2
        return n1
