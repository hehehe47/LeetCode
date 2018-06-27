'''
Q:https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

timestamp:2018-6-26 20:12:07
'''


def find(s, words):
    '''
    :param s: str
    :param words: list[str]
    :return: list[int]
    '''
    a = len(words[0])
    b = a * len(words)
    c, l = [], []
    # ===============
    # import itertools
    # for i in itertools.permutations(words,len(words)):
    #     st = ''
    #     for j in i:
    #         st+=j
    #     l.append(st)
    # print(l)
    # ===============

    if not s or not words or '' in words:
        return c
    i = 0
    # 超时
    # while i<=len(s)-b:
    #     sub = s[i:b+i]
    #     # ===========
    #     # g = words.copy()
    #     # for w in g:
    #     #     if w not in sub:
    #     #         break
    #     #     else:
    #     #         idx = sub.index(w)
    #     #         sub = sub[0:idx]+'1'+sub[idx+a:]
    #     # ===========
    #     while sub[0:g] in g:
    #         g.pop(g.index(sub[0:a]))
    #         sub = sub[a:]
    #         if sub[len(sub)-a:len(sub)] in g:
    #             g.pop(g.index(sub[0:a]))
    #             sub = sub[a:]
    #             if sub[len(sub)-a:len(sub)] in g:
    #                 g.pop(g.index(sub[len(sub)-a:len(sub)]))
    #                 sub = sub[:len(sub)-a]
    #             else:
    #                 break
    #     if not sub:
    #         c.append(i)
    #     i+=1
    # return c
    l1 = [s[i:i+1] for i in range(0,len(s)-a+1,a)]
    l2 = [s[i:i+1] for i in range(a-1,len(s),a)]
    print(l1)
    print(l2)

print(find('barfoofoobarthefoobarman',['foo','bar','the']))
print(find('wordgoodgoodgoodbestword',['word','good','best','good']))
print(find('barfoothefoobarman',['foo','bar']))
print(find('ababaab',['ab','ba','ba']))