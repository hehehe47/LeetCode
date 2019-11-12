def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    l1 = l2 = head
    # 两次循环
    # count = 0
    # while l2:
    #     count += 1
    #     l2 = l2.next
    # c = count - n
    # if c == 0:
    #     return head.next
    # i = 1
    # while l1 and i < c:
    #     l1 = l1.next
    #     i += 1
    # l1.next = l1.next.next
    # return head

    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    l1 = l2 = head
    for i in range(n + 1):
        if not l2:
            return head.next
        l2 = l2.next
    while l2:
        l2 = l2.next
        l1 = l1.next
    l1.next = l1.next.next
    return head
