class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}

        #bucket sort
        #trying to map count-> values

        #first get count of each items
        #values->count
        for num in nums:
            count[num]=1+count.get(num,0)

        freq=[[] for i in range(len(nums)+1)]

        for num,cnt in count.items():
            freq[cnt].append(num)
            #count-> value mapping
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

        
        