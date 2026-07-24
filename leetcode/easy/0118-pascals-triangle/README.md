# Pascal's Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `numRows`, return the first numRows of  **Pascal's triangle**.

In  **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

 **Example 1:** 

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```

 **Example 2:** 

```
Input: numRows = 1
Output: [[1]]

```

 

 **Constraints:** 

- 1 <= numRows <= 30

## Solution

**Language:** Java  
**Runtime:** 1 ms (beats 94.34%)  
**Memory:** 43.5 MB (beats 52.53%)  
**Submitted:** 2026-07-24T06:51:46.639Z  

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 0) return new ArrayList<>();
        if (numRows == 1) {
            List<List<Integer>> result = new ArrayList<>();
            result.add(Arrays.asList(1));
            return result;
        }
        
        List<List<Integer>> prevRows = generate(numRows - 1);
        List<Integer> newRow = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            newRow.add(1);
        }
        
        for (int i = 1; i < numRows - 1; i++) {
            newRow.set(i, prevRows.get(numRows - 2).get(i - 1) + prevRows.get(numRows - 2).get(i));
        }
        
        prevRows.add(newRow);
        return prevRows;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/pascals-triangle/)