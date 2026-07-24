# Pascal's Triangle II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed**) row of the  **Pascal's triangle**.

In  **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

 **Example 1:** 

```
Input: rowIndex = 3
Output: [1,3,3,1]

```

 **Example 2:** 

```
Input: rowIndex = 0
Output: [1]

```

 **Example 3:** 

```
Input: rowIndex = 1
Output: [1,1]

```

 

 **Constraints:** 

- 0 <= rowIndex <= 33

 

 **Follow up:**  Could you optimize your algorithm to use only `O(rowIndex)` extra space?

## Solution

**Language:** Java  
**Runtime:** 2 ms (beats 27.11%)  
**Memory:** 42.5 MB (beats 72.19%)  
**Submitted:** 2026-07-24T06:52:19.102Z  

```java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        row.add(1);

        for (int i = 0; i < rowIndex; i++) {
            List<Integer> newRow = new ArrayList<>();
            newRow.add(1);
            for (int j = 1; j < row.size(); j++) {
                newRow.add(row.get(j - 1) + row.get(j));
            }
            newRow.add(1);
            row = newRow;
        }

        return row;        
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/pascals-triangle-ii/)