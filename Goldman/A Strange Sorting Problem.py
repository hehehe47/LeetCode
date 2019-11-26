#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/14 16:55 
# @Author : Patrick 
# @File : A Strange Sorting Problem.py 
# @Software: PyCharm

def strangeSort1(mapping, nums):
    # Write your code here
    new_map = {}
    new_nums = []
    map_num_new = {}
    result = []
    for idx, num in enumerate(mapping):
        new_map[num] = idx
    for raw in nums:
        s = ''
        for digit in raw:
            s += str(new_map[int(digit)])
        new_nums.append(s)
        map_num_new[s] = raw
    new_nums.sort(key=int)
    for j in new_nums:
        result.append(map_num_new[j])
    return result


# def reveal_true_num(s, map):
#     str_num = ''
#     for digit in s:
#         str_num += str(map[digit])
#     return int(str_num)
#
#
# def strangeSort(mapping, nums):
#     dmap, m = {}, {}
#     for idx, num in enumerate(mapping):
#         dmap[str(num)] = idx
#     for i in nums:
#         m[i] = reveal_true_num(i, dmap)
#     return sorted(m, key=m.get)


def reveal(s, map):
    str_num = ''
    for digit in s:
        str_num += str(map[digit])
    return str_num


def strangeSort(mapping, nums):
    dmap, transfer = {}, {}
    new_nums, ans = [], []
    for idx, num in enumerate(mapping):
        dmap[str(num)] = idx
    for i in nums:
        transfer[reveal(i, dmap)] = i
        new_nums.append(reveal(i, dmap))
    new_nums.sort(key=int)
    return [transfer[j] for j in new_nums]


print(strangeSort1([2, 1, 4, 8, 6, 3, 0, 9, 7, 5], ['12', '02', '4', '023', '65', '83', '224', '50']))
print(strangeSort([2, 1, 4, 8, 6, 3, 0, 9, 7, 5], ['12', '02', '4', '023', '65', '83', '224', '50']))
