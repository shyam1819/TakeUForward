class Solution:
    def reverseNumber(self, n):
        sign = -1 if n<0 else 1
        n = abs(n)
        reverse_number = 0
        while n>0:
            digit = n%10
            n = n//10
            reverse_number = reverse_number*10 + digit
        return reverse_number
