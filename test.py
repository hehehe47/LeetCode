# strs = ['ab', 'ded', 'as']
#
# for i, j in zip(range(len(strs)), range(len(min(strs)))):
#     print(i, j)
#
# print(ord('a'))
#
# print(2 ^ 4)
#
# print(int('inf')>1000000000000000000)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l = ListNode(1)
# l = l.next

a = 1
# c = [1, l.next.val][not l.next]
c = l.val if l else 0
d = [0, l.val][not l]
print(c)
print(7 / 10)
print(7 // 10)
d = {1: 2}
print(type(d.keys()))
