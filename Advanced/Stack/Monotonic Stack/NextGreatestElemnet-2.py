class Solution:
    def nextGreaterElements(self, arr):
        n = len(arr)
        res = [-1]*n
        stack = [i for i in range(n-1,-1,-1)]
        for i in range(n-1,-1,-1):
            while stack and arr[i]>=arr[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = arr[stack[-1]]
            stack.append(i)
        return res
      
