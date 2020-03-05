#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/5 15:44 
# @Author : Patrick 
# @File : 1007. Minimum Domino Rotations For Equal Row.py 
# @Software: PyCharm


class Solution:
    def sol(self, A, B) -> int:
        def check(x):
            rota_a, rota_b = 0, 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    rota_b += 1
                if B[i] != x:
                    rota_a += 1
            return min(rota_b, rota_a)

        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])

    def minDominoRotations(self, A, B) -> int:

        def succ(origin, target, num):
            for i in range(len(origin)):
                if (origin[i] != num and target[i] == num) or origin[i] == num:
                    continue
                else:
                    return False
            return True

        dc1, dc2 = {}, {}
        for num in A:
            if num not in dc1:
                dc1[num] = 1
            else:
                dc1[num] += 1
        for num in B:
            if num not in dc2:
                dc2[num] = 1
            else:
                dc2[num] += 1
        d = {}
        for k, v in dc1.items():
            if v not in d:
                d[v] = [(1, k)]
            else:
                d[v].append((1, k))
        for k, v in dc2.items():
            if v not in d:
                d[v] = [(2, k)]
            else:
                d[v].append((2, k))
        d = sorted(d.items(), key=lambda d: d[0], reverse=True)
        for time, pairs in d:
            for idx, num in pairs:
                ori, tar = [(A, B), (B, A)][idx == 2]
                if succ(ori, tar, num):
                    return len(A) - time
        return -1


s = Solution()
# print(s.sol(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))
# print(s.sol(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]))
print(s.sol(A=[1, 2, 1, 1, 1, 2, 2, 2]
            , B=[2, 1, 2, 2, 2, 2, 2, 2]))
