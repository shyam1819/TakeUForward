class Solution:
    def reverse(self, arr: list, n: int) -> None:
        # Start pointer at index 0
        left = 0
        # End pointer at index n-1
        right = n - 1
        
        # Continue until pointers meet in the middle
        while left < right:
            # Swap the elements
            arr[left], arr[right] = arr[right], arr[left]
            
            # Move pointers closer to each other
            left += 1
            right -= 1
