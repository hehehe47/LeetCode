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

# import java.util.HashMap;
#
# public
#
#
# class Solution
#     {
#     // METHOD
#     SIGNATURE
#     BEGINS, THIS
#     METHOD
#     IS
#     REQUIRED
#     public
#     ALNode
#     deepCopy(ALNode
#     head)
#     {
#     if (head == null)
#
#
# return null;
# HashMap < ALNode, ALNode > map = new
# HashMap <> ();
#
# ALNode
# ans = new
# ALNode(head.value);
# ans.next = head.next;
# ans.arbitrary = head.arbitrary;
#
# map.put(head, ans);
#
# ALNode
# p = head, q = ans;
# while (p.next != null){
# q.next = new ALNode();
# q.next.value = p.next.value;
# map.put(p.next, q.next);
# p = p.next;
# q = q.next;
# }
#
# p = head;
# q = ans;
# while (q != null){
# q.arbitrary = map.get(p.arbitrary);
# p = p.next;
# q = q.next;
# }
# return ans;
# }
#
# // METHOD
# SIGNATURE
# ENDS
# }
