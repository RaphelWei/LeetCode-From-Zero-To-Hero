# 217.Constains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.
### Example 1
```
Input: nums = [1,2,3,1]
Output: true
```
## Solution Sketch
This problem is straightforward. We can use a hashmap to track each `unique` number. If a number is already in the hashmap, then we return true.
## Result
+ Time Complexity: O(n)
+ Space Complexity: O(n)