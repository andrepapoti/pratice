from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       cmpSet = set(nums)
       return len(nums) == len(cmpSet)