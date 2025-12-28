class Solution:
    def primeUptoN(self, n):
        if n<2:
            return []
        is_prime = [True]*(n+1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p**2 <= n:
            if is_prime[p**2]:
                for i in range(p**2,n+1,p):
                    is_prime[i] = False
            p+=1
        return sum(is_prime)
