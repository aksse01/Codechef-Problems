# Populating Next Right Pointers in Each Node II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary tree

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

 

 **Example 1:** 

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

```

 **Example 2:** 

```
Input: root = []
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 6000].
- -100 <= Node.val <= 100

 

 **Follow-up:** 

- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Solution

**Language:** Java  
**Runtime:** 1 ms (beats 62.09%)  
**Memory:** 46.4 MB (beats 18.53%)  
**Submitted:** 2026-07-24T06:51:11.340Z  

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root==null)return root;
        Queue<Node>queue=new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int len=queue.size();
            Node prev=null;
            for(int i=0;i<len;i++){
                Node cur=queue.poll();
                if(prev!=null){
                    prev.next=cur;
                }
                prev=cur;
                if(cur.left!=null)queue.offer(cur.left);
                if(cur.right!=null)queue.offer(cur.right);
            }
            prev.next=null;
        }
        return root;
    }
}
```

---

[View on LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)