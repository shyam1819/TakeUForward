class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        i = 0
        buckets = {}
        max_fruits = 0
        
        # j is our 'right' pointer, expanding the window
        for j in range(len(fruits)):
            # Add the current fruit to our count
            buckets[fruits[j]] = buckets.get(fruits[j], 0) + 1
            
            # If we have more than 2 types of fruit, shrink from the left
            while len(buckets) > 2:
                buckets[fruits[i]] -= 1
                if buckets[fruits[i]] == 0:
                    del buckets[fruits[i]]
                i += 1 # Move the left pointer forward
            
            # Calculate the current window size and update the max
            max_fruits = max(max_fruits, j - i + 1)
            
        return max_fruits
