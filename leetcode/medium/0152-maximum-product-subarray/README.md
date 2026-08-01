# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return  *the product*.

The test cases are generated so that the answer will fit in a  **32-bit**  integer.

 **Note**  that the product of an array with a single element is the value of that element.

 

 **Example 1:** 

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

 **Example 2:** 

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

## Solution

**Language:** Java  
**Runtime:** 2 ms (beats 71.50%)  
**Memory:** 47.2 MB (beats 73.75%)  
**Submitted:** 2026-08-01T05:53:18.840Z  

```java
class Solution {
    public int maxProduct(int[] nums) {
     int currmax = nums[0];
     int currmin = nums[0];
     int maxnum = nums[0];
     for(int i=1;i<nums .length;i++)
     {
        int tempmax = currmax;
        currmax = Math.max(nums[i],Math.max(currmax*nums[i],currmin*nums[i]));
        currmin = Math.min(nums[i],Math.min(tempmax*nums[i],currmin*nums[i]));
        maxnum = Math.max(maxnum,currmax);

     }
     return maxnum;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)