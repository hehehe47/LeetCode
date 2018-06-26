'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

timestamp:2018-6-26 19:42:40
'''


def vaild(s):
    '''
    :param s: str 
    :return: int
    '''
    i, j = [a for a, b in enumerate(s) if b == '('], [a for a, b in enumerate(s) if b == ')']
    l = []
    # i为左括号位置，j为右括号位置
    if not i or not j:
        return 0
    for a in range(len(i)):
        for b in range(len(j) - 1, -1, -1):
            if a < b:
                print(i[a], j[b])
                sub = s[i[a]:j[b] + 1]
                if (j[b] + 1 - i[a]) % 2 != 0:
                    continue
                for k in sub:
                    if k == '(':
                        l.append(k)
                    else:
                        if l[len(l) - 1] == '(':
                            l.pop()
                if not l:
                    return j[b] + 1 - i[a]
                print(sub)


# print(vaild(')()())'))
print(vaild('(()'))
