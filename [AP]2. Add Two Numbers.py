class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ll1, ll2 = l1, l2
    flag = False
    l = l11 = ListNode(0)
    count = 0
    s = 0
    while ll1 or ll2:
        if flag:
            s += 1
        flag = False
        if ll1:
            a = ll1.val
        else:
            a = 0
        if ll2:
            b = ll2.val
        else:
            b = 0
        # a=[0,ll1.val][not ll1]
        # print(ll2)
        # b=[0,ll2.val][not ll2]

        s = a + b + s
        if s >= 10:
            flag = True
            s -= 10
        # if count == 0:
        #     l = ListNode(s)
        # else:
        l11.next = ListNode(s)
        l11 = l11.next
        s = 0
        if ll1:
            ll1 = ll1.next
        if ll2:
            ll2 = ll2.next
        count += 1
    if flag:
        l11.next = ListNode(1)
    return l.next


# def addTwoNumbers(self, l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     p, q = l1, l2
#     head = l = ListNode(0)
#     s, c = 0, 0
#     while p or q:
#         a = p.val if p else 0
#         b = q.val if q else 0
#
#         s = a + b + c
#
#         c = s // 10
#
#         l.next = ListNode(s % 10)
#         l = l.next
#
#         if p:
#             p = p.next
#         if q:
#             q = q.next
#     if c > 0:
#         l.next = ListNode(c)
#
#     return head.next


l1 = l3 = ListNode(2)
l4 = ListNode(4)
l3.next = l4
l3 = l3.next
l4 = ListNode(3)
l3.next = l4
l2 = l3 = ListNode(5)
l4 = ListNode(6)
l3.next = l4
l3 = l3.next
l4 = ListNode(4)
l3.next = l4

print(addTwoNumbers(l1, l2))
