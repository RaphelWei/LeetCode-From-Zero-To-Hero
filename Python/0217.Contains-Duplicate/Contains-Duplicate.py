from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for x in nums:
            if x in h:
                return True
            else:
                h[x] = 0
                
        return False

sol = Solution()
nums = [1,2,3,4]
print(sol.containsDuplicate(nums))