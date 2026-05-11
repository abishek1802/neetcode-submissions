class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map={}
        for index,value in enumerate(nums):
            diff=target-value
            if diff in Map:
                return [Map[diff],index]
            Map[value]=index
        