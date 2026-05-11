class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dash = set(nums)
        if len(dash)!=len(nums):
            return True
        return False
    
        