# Min Stack

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- MinStack() initializes the stack object.
- void push(int value) pushes the element value onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

 

 **Example 1:** 

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

```

 

 **Constraints:** 

- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.

## Solution

**Language:** Java  
**Runtime:** 31 ms (beats 79.61%)  
**Memory:** 104.7 MB (beats 6.54%)  
**Submitted:** 2026-08-01T05:54:29.752Z  

```java
// import java.util.ArrayList;

class MinStack {
    ArrayList<Integer> arr;
    ArrayList<Integer> mini;

    public MinStack() {
        arr = new ArrayList<>();
        mini = new ArrayList<>();
    }

    public void push(int value) {
        arr.add(value);

        if (mini.isEmpty()) {
            mini.add(value);
        } else {
            mini.add(Math.min(mini.get(mini.size() - 1), value));
        }
    }

    public void pop() {
        if (!arr.isEmpty()) {
            arr.remove(arr.size() - 1);
            mini.remove(mini.size() - 1);
        }
    }

    public int top() {
        if (arr.isEmpty()) {
            return -1;   // or throw exception
        }
        return arr.get(arr.size() - 1);
    }

    public int getMin() {
        if (mini.isEmpty()) {
            return -1;   // or throw exception
        }
        return mini.get(mini.size() - 1);
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/min-stack/)