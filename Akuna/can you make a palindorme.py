#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/21 21:24 
# @Author : Patrick 
# @File : can you make a palindorme.py 
# @Software: PyCharm

def ispalindrome(s, k):
    count = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            count += 1
    print(count)
    if count > k:
        return False
    else:
        return True


def palindromeChecker(s, l, r, k):
    # Write your code here
    ans = ''
    for i in range(len(l)):
        if ispalindrome(s[l[i]:r[i] + 1], k[i]):
            ans += '1'
        else:
            ans += '0'
    return ans


# print(palindromeChecker('bcbab', [1, 1, 2], [4, 3, 3], [3, 3, 0]))
s = 'aaaaagbbbbb'
print(palindromeChecker(s, [0], [len(s) - 1], [0]))
