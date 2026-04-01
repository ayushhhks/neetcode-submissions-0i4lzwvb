class Solution:
    def findMin(self, nums: List[int]) -> int:
        beg, end = 0, len(nums) - 1
        
        # If the array isn't rotated at all
        if nums[beg] <= nums[end]:
            return nums[beg]
        
        while beg < end:
            mid = (beg + end) // 2
            
            # If mid is greater than the end, the minimum is in the right half
            if nums[mid] > nums[end]:
                beg = mid + 1
            # Otherwise, the minimum is at mid or to the left
            else:
                end = mid
                
        return nums[end]
        