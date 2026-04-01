class Solution:
    def maxArea(self, heights):
        l = 0
        r = len(heights) - 1
        water = 0

        while l < r:

            area = min(heights[l], heights[r]) * (r - l)
            water = max(water, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return water
            
            

           

        