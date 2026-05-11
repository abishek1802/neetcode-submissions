class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        Count={}

        for i in nums:
            Count[i]=1+Count.get(i,0)
        
        freq=[[] for i in range(len(nums)+1)]

        for num,cnt in Count.items():
            freq[cnt].append(num)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

        