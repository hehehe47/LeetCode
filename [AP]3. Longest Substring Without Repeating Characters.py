def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # if not s:
    #     return 0
    # elif len(s)==1:
    #     return 1
    # i, l,m = 0, 1,0
    # j = i + 1
    # d = {s[i]: 0}
    # # d[s[i]] = True
    # while j < len(s):
    #     if s[j] not in d.keys():
    #         d[s[j]] = j
    #         j += 1
    #         l += 1
    #     else:
    #         i = d[s[j]]+1
    #         j = i + 1
    #         d = {s[i]: i}
    #         l = 1
    #     if l>m:
    #         m = l
    # return m

    m, start = 0, -1
    d = {}
    for i in range(len(s)):
        if s[i] in d and d[s[i]] > start:
            start = d[s[i]]
        else:
            if m < i - start:
                m = i - start
        d[s[i]] = i
    return m


print(lengthOfLongestSubstring("dvdf"))
