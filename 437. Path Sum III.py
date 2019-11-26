#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/12 16:29 
# @Author : Patrick 
# @File : 437. Path Sum III.py 
# @Software: PyCharm


class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, root, s):
        # if not root:
        #     return count
        # if root.val in need_to_find:
        #     need_to_find.remove(root.val)
        #     count += 1
        # else:
        #     need_to_find.remove(s - v)
        # need_to_find.add(s - root.val)
        # cs += root.val
        # need_to_find.add(s - cs)
        # # need_to_find.add(sum-root.val)
        # count = self.helper(root.left, count, need_to_find, s, cs, root.val)
        # count = self.helper(root.right, count, need_to_find, s, cs, root.val)
        # need_to_find.remove(s - root.val)
        # need_to_find.remove(s - cs)
        # return count
        res = 0
        if not root:
            return res

        l = self.helper(root.left, s - root.val)
        r = self.helper(root.right, s - root.val)
        if root.val == s:
            res += 1

        return res + l + r


s = Solution()

root = TreeNode(10,
                TreeNode(5,
                         TreeNode(3,
                                  TreeNode(3, None, None), TreeNode(-2, None, None)),
                         TreeNode(2, None,
                                  TreeNode(1, None, None))),
                TreeNode(-3, None,
                         TreeNode(11, None, None)))

print(s.pathSum(root, 8))
