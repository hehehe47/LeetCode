'''
Q:https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

timestamp:2018-6-26 20:00:20
'''


def letter(digits):
    '''
    :param digits:str 
    :return: list[str]
    '''
    digits = digits.replace('1', '').replace('0', '')
    if not digits:
        return []
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    r = [x for x in d[digits[0]]]  # 初始化第一位
    # print(r)
    for i in digits[1:]:
        tmp2 = r.copy()
        r = ['']
        for a in tmp2:
            for b in d[i]:
                if not r[0]:
                    r.remove(r[0])
                if (a + b).isalpha():
                    r.append(a + b)
    return r


print(letter('123'))
