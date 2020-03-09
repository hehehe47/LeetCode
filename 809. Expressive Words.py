#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/5 17:41 
# @Author : Patrick 
# @File : 809. Expressive Words.py 
# @Software: PyCharm


class Solution:
    def expressiveWords(self, S, words) -> int:
        count = 0

        for word in words:
            tmp1, tmp2 = S, word
            flag = False
            while tmp2:
                if tmp1[0] == tmp2[0]:
                    diff = len(tmp1) - len(tmp1.lstrip(tmp1[0])) - (len(tmp2) - len(tmp2.lstrip(tmp2[0])))
                    diff1 = len(tmp1) - len(tmp1.lstrip(tmp1[0]))
                    tmp1 = tmp1.lstrip(tmp1[0])
                    tmp2 = tmp2.lstrip(tmp2[0])
                    if diff != 0 and diff1 < 3:
                        flag = False
                        break
                    else:
                        flag = True
                else:
                    flag = False
                    break
                if flag and not tmp1:
                    count += 1
        print(count)


s = Solution()
# s.expressiveWords(S="heeellooo",
#                   words=["hello", "hi", "helo"])
# s.expressiveWords("abcd",
#                   ["abc"])
# s.expressiveWords("dddiiiinnssssssoooo",
# ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"])
s.expressiveWords("aaa",
                  ["aaaa"])
