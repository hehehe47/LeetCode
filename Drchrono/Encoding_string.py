#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/18 16:37 
# @Author : Patrick 
# @File : Encoding_string.py 
# @Software: PyCharm

# s = ord('z')
def encoding(char1, char2):
    num_char1, num_char2 = ord(char1) - 96, ord(char2) - 96
    if (num_char1 + num_char2) % 26 == 0:
        tmp = 26 + 96
    else:
        tmp = (num_char1 + num_char2) % 26 + 96
    return chr(tmp)


def encode_string(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    l_s = list(s)
    after_dup = [i for i in set(s) if i not in vowels]
    after_dup.sort(key=l_s.index)
    if len(after_dup) < 1:
        return None
    ans = ''
    after_dup.append(after_dup[0])
    for idx in range(len(after_dup) - 1):
        ans += encoding(after_dup[idx], after_dup[idx + 1])
    return ans


# s = 'aaaaaeeee'
s = 'jklejlkenlasienfnabde'
# s = 'yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxioioioioio'
print(encode_string(s))
