class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for x in nums:
            count[x]=1+count.get(x,0)

        freq=[[]for i in range(len(nums)+1)]
        
        for v,c in count.items():
            freq[c].append(v)

        res=[]

        for x in range(len(freq)-1,0,-1):
            for y in freq[x]:
                res.append(y)
                if len(res)==k:
                    return res