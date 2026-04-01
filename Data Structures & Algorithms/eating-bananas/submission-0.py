import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Binary search range
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed at speed 'mid'
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours <= h:
                # Speed works, try to find a smaller speed
                high = mid - 1
            else:
                # Speed too slow, must increase it
                low = mid + 1
        
        return low