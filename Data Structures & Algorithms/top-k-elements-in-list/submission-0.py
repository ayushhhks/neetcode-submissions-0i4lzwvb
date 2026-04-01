from collections import defaultdict
class Solution:
    ##my solution TC is O(nlogn) and SC is O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            if num not in seen:
                seen[num]=1
            else:
                seen[num]+=1
        
        sorted_keys = sorted(seen, key=seen.get , reverse=True)
           ##key=seen.get helps sorting by key and in ascending values not descending
        return sorted_keys[:k]
                