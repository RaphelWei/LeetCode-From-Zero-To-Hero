# 1. Two Sum
## Problem Description
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly one solution***, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
## Solution Sketch
For each element `x` in the list, we can get its `complement`:

```
complement = target - x
```

The brute force startegy is that, we can compare each element in the list with the `complement`, which will be O(n^2).

To reduce the time complexity, we can use `HashMap` to solve this problem.

Firstly, we linearly scan the list. For each element `x`, if its complement is already in the hashmap, we directly output the index of the `complement` and `x`. Otherwise, we store `x` in the hashmap.  
## Result
+ Time Complexity: O(n)
+ Space Complexity: O(n)