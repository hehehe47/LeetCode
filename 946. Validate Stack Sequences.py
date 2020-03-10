#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/9 22:40 
# @Author : Patrick 
# @File : 946. Validate Stack Sequences.py 
# @Software: PyCharm


class Solution:
    # def validateStackSequences(self, pushed, popped):
    #     start, end = 0, -1
    #     tmp_stack = []
    #     for po in popped:
    #         end = pushed.index(po)
    #         # if end < start:
    #         #     return False
    #         tmp_stack += pushed[start:end + 1]
    #         tmp_set = set(tmp_stack)
    #
    #         if po != tmp_stack[-1]:
    #             return False
    #         else:
    #             tmp_stack.pop()
    #             tmp_set.remove(po)
    #         start = end + 1 if end + 1 > start else start
    #     return True

    def validateStackSequences(self, pushed, popped) -> bool:
        stack_len = len(pushed)
        stack = []
        i, j = 0, 0
        while i < stack_len and j < stack_len:
            # 遍历是否压栈
            while not stack or popped[j] != stack[-1] and i < stack_len:
                stack.append(pushed[i])
                i = i + 1
            # 遍历是否弹栈
            while stack and popped[j] == stack[-1] and j < stack_len:
                stack.pop()
                j = j + 1
        print("i,j:{},{}".format(i, j))
        if i == j:
            return True


s = Solution()
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))  # True
print(s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))  #
print(s.validateStackSequences([0, 2, 1, 3], [1, 2, 3, 0]))  # True
print(s.validateStackSequences([3, 1, 0, 2], [2, 0, 3, 1]))  #
print(s.validateStackSequences([4, 0, 1, 2, 3], [4, 2, 3, 0, 1]))  #
print(s.validateStackSequences([2, 1, 0], [2, 1, 0]))  # True
#
