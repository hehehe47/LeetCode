#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/7 16:01
# @Author : Patrick
# @File : 1110. Delete Nodes And Return Forest.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x=None, y=None, z=None):
        self.val = x
        self.left = y
        self.right = z


class Solution:
    def __init__(self):
        self.ans = []
        self.delete = set()

    def helper(self, root, is_root):
        if not root: return None
        root_deleted = root.val in self.delete
        if is_root and not root_deleted:
            self.ans.append(root)
        root.left = self.helper(root.left, root_deleted)
        root.right = self.helper(root.right, root_deleted)
        return None if root_deleted else root

    def delNodes(self, root, to_delete):
        self.delete = set(to_delete)
        self.helper(root, True)
        return self.ans


s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)),
                TreeNode(3, TreeNode(6, None, None), TreeNode(7, None, None)))

print(s.delNodes(root, to_delete=[3, 5]))
