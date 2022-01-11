from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)
        for i in range(n):
            y = target - nums[i]
            if y in h:
                return [h[y],i]
            h[nums[i]] =i

sol = Solution()
# test example 1
nums = [2,7,11,15]
target = 9
# expected output: [0,1]
print(sol.twoSum(nums, target))

# test example 2
nums = [3,2,4]
target = 6
# expected output: [1,2]
print(sol.twoSum(nums, target))

# test example 1
nums = [3,3]
target = 6
# expected output: [0,1]
print(sol.twoSum(nums, target))
