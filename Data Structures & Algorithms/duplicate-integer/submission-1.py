class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            if num in seen:
                return True
            seen[num]=i
        return False