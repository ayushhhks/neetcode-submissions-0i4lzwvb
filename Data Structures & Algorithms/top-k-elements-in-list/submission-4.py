class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies - O(N)
        count = Counter(nums)
        
        # 2. Build a Min-Heap of size K - O(N log K)
        # We store (frequency, element)
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            
            # If heap size exceeds k, pop the smallest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3. Extract elements from heap - O(K log K)
        return [item[1] for item in heap]