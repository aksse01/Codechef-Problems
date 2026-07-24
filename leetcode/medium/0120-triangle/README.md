# Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a `triangle` array, return  *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

 

 **Example 1:** 

```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

```

 **Example 2:** 

```
Input: triangle = [[-10]]
Output: -10

```

 

 **Constraints:** 

- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -104 <= triangle[i][j] <= 104

 

 **Follow up:**  Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

## Solution

**Language:** Java  
**Runtime:** 3 ms (beats 80.23%)  
**Memory:** 45.7 MB (beats 39.80%)  
**Submitted:** 2026-07-24T06:53:43.061Z  

```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int row = triangle.size();
        int[] memo = new int[row];

        for (int i = 0; i < row; i++) {
            memo[i] = triangle.get(row - 1).get(i);
        }

        for (int r = row-2; r >= 0; r--) {
            for (int c = 0; c <= r; c++) {
                memo[c] = Math.min(memo[c], memo[c+1]) + triangle.get(r).get(c);
            }
        }

        return memo[0];        
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/triangle/)