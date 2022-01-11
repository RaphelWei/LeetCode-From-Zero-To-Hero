# 2103.Rings and Rods

## Problem Description
There are `n` rings and each ring is either red, green, or blue. The rings are distributed **across ten rods** labeled from 0 to 9.

You are given a string `rings` of length `2n` that describes the `n` rings that are placed onto the rods. Every two characters in `rings` forms a **color-position pair** that is used to describe each ring where:

+ The **first** character of the `i-th` pair denotes the `i-th` ring's **color** (`'R'`, `'G'`, `'B'`).
+ The **second** character of the `i-th` pair denotes the **rod** that the `i-th` ring is placed on (`'0'` to `'9'`).
For example, `"R3G2B1"` describes `n == 3` rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

Return *the number of rods that have **all three colors** of rings on them*.

### Example 1
```
Input: rings = "B0B6G0R6R0R6G9"
Output: 1
Explanation: 
- The rod labeled 0 holds 3 rings with all colors: red, green, and blue.
- The rod labeled 6 holds 3 rings, but it only has red and blue.
- The rod labeled 9 holds only a green ring.
Thus, the number of rods with all three colors is 1.
```

## Solution Sketch
We will use the `or` boolean operator to solve this problem.

There are 10 rods in total in this problem, we use an array of length 10 to store the status of each rod.

Since we have 'R', 'G',and 'B' three colors, we use 3 bits to represent each of these colors. At the beginning, all the 3 bits will be initialized to 0 (which is 000). If a rod has a red ring, we set the right most bit to 1 (001), which is equivalent to `or` 001 (which is 1). Similarly, if a rod has a green ring, we `or` it with 010 (which is 2); and we `or` a 100 (which is 4) if it has a blue ring.

Then it is obvious that if a rod has all 3 rings, then its status must be 111 (which is 7).
## Results
+ Time Complexity: $O(n)$
+ Space Complexity: $O(10)$