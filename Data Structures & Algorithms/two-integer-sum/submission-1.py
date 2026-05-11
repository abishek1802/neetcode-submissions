class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for index,value in enumerate(nums):
            diff=target-value
            if diff in hmap:
                return [hmap[diff],index]
            hmap[value]=index