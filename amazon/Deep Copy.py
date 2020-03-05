#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/6 15:41 
# @Author : Patrick 
# @File : Deep Copy.py 
# @Software: PyCharm

class ALNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.arbitrary = None


def deepCopy(head):
    # WRITE YOUR CODE HERE
    if not head:
        return None
    d = {}
    p = q = head
    while p:
        d[p] = ALNode(p.value)
        p = p.next
    while q:
        d[q].next = d.get(q.next)
        d[q].arbitrary = d.get(q.arbitrary)
        q = q.next
    return d.get(head)

