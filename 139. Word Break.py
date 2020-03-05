#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/26 22:15 
# @Author : Patrick 
# @File : 139. Word Break.py 
# @Software: PyCharm


# 139
# s = "leetcode"
# wordDict = ["leet", "code"]

# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]


# s = "abcd"
# wordDict = ["a", "abc", "b", "cd"]
#

# s = "applepenapple"
# wordDict = ["apple", "pen"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]


# s = "cars"
# wordDict = ["car", "ca", "rs"]

# s = "aaaaaaa"
# wordDict = ["aaaa", "aaa"]


class Solution:
    letter_len = {}
    cant_set = set()

    def wordBreak(self, s, wordDict):
        for word in wordDict:
            if word[0] not in self.letter_len:
                self.letter_len[word[0]] = [len(word)]
            else:
                self.letter_len[word[0]].append(len(word))
        for k, v in self.letter_len.items():
            self.letter_len[k] = sorted(v, reverse=True)
        wordDict = set(wordDict)
        a = self.helper(0, len(s), s, wordDict)
        # print(self.cant_set)
        return a

    def helper(self, start, end, s, wordDict):
        if start == end:
            return True
        elif start > end:
            return False
        ans = False
        if s[start] not in self.letter_len:
            self.cant_set.add(s[start:])
            return False
        if s[start:end] in self.cant_set:
            return False
        for length in self.letter_len[s[start]]:
            tmp = s[start:start + length]
            if tmp in wordDict:
                ans = self.helper(start + length, end, s, wordDict)
            if ans:
                start = end
        if not ans:
            self.cant_set.add(s[start:end])
        return ans


s = "a"
wordDict = ["a"]
a = Solution()
print(a.wordBreak(s, wordDict))
