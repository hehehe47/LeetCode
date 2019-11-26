#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/15 21:00 
# @Author : Patrick 
# @File : Number scores.py 
# @Software: PyCharm

def rule_even(n):
    count = 0
    for i in n:
        if int(i) % 2 == 0:
            count += 3
    return count


def small(n):
    l = []
    for i in n:
        if l and ord(i) - ord(l[-1][-1]) == -1:
            l[-1] += i
        else:
            l.append(i)

    return sum(len(s) ** 2 for s in l)


def count_two(n):
    ans = 0
    for i in range(len(n)):
        if i != 0 and n[i] == '2' and n[i - 1] == '2':
            ans += 6
    return ans


def compute_number_score(number):
    score = 0
    number = str(number)
    score += 5 * number.count('7')  # rule 1
    # score += (6 * (number.count('2') - 1) if number.count(2) > 1 else 0)  # rule 2
    score += count_two(number)  # rule 2
    score += rule_even(number)  # rule 5
    score += 4 if int(number) % 3 == 0 else 0  # rule 4
    score += small(number)

    return score


print(compute_number_score(321222158))  # 44
print(compute_number_score(1075456))  # 25
print(compute_number_score(22222))  # 44
