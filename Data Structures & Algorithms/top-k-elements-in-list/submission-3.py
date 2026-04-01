from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        
        sorted_seen = sorted(seen, key=seen.get, reverse=True)

        return sorted_seen[:k]
          
