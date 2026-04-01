class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##this is HOW you do Bucket Sort--
        count={}
        ## first we will count teh freq using hashmap only
        freq=[[] for i in range(len(nums)+1)]
        ##array for bucket sort

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
        