class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##this is using Bucket Sort--
        count={}
        ## first we will count teh freq using hashmap only
        freq=[[] for i in range(len(nums)+1)]
        ##array for bucket sort, creates a seconfd array luke buxckets and add thibgs to it inn this case the bucket number
        ## is frequency and the items in a bucket are numbers that have that much frequency

        ##counting freq
        for n in nums:
            count[n]=1+count.get(n,0)
        
        ##adding in valuefrequency array / Bucket Sort logic core, we add the elemnet based on their freq
        for n,c in count.items():
            freq[c].append(n)
        
        ##storing result, top k elements
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        