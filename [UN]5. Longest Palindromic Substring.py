def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # d={}
    # c=[]
    # for i in range(len(s)):
    #     if s[i] not in d:
    #         d[s[i]] = [i]
    #     else:
    #         d[s[i]].append(i)
    # m = 1
    # for l in d.values():
    #     if l[len(l)-1]-l[0]>m:
    #         for i in range(l[0],l[len(l)-1]):
    #             if s[i]!= s[l[len(l)-1]-i+l[0]]:
    #                 break
    #         m = l[len(l)-1]-l[0]+1
    #         c = l
    #
    # return s[c[0]:c[len(c)-1]+1]


print(longestPalindrome('askdljfabcdedcbaeeeeeeeeeeeeeeee'))
