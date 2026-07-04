class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count-> items
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for items in nums:
            count[items]=count.get(items,0)+1

        for item,cnt in count.items():
            freq[cnt].append(item)

        res=[]

        for i in range(len(freq)-1,0,-1):

            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res

