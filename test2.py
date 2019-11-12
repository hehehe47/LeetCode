k = 7
MAX = 2 ** k


def decr(value, size):
    if size <= value:
        return value - size
    else:
        return MAX - (size - value)


def between(value, init, end):
    if init == end:
        return True
    elif init > end:
        return not (init >= value > end)
    return init < value < end


def Ebetween(value, init, end):
    if value == init:
        return True
    else:
        return between(value, init, end)


def betweenE(value, init, end):
    if value == end:
        return True
    else:
        return between(value, init, end)


class Node:
    def __init__(self, id):
        self.id = id
        self.finger = {}
        self.start = {}
        for i in range(k):
            self.start[i] = (self.id + (2 ** i)) % (2 ** k)

    def successor(self):
        return self.finger[0]

    def find_successor(self, id):
        if betweenE(id, self.predecessor.id, self.id):
            return self
        n = self.find_predecessor(id)
        return n.successor()

    def find_predecessor(self, id):
        if id == self.id:
            return self.predecessor
        n1 = self
        while not betweenE(id, n1.id, n1.successor().id):
            n1 = n1.closest_preceding_finger(id)
        return n1

    def closest_preceding_finger(self, id):
        for i in range(k - 1, -1, -1):
            if between(self.finger[i].id, self.id, id):
                return self.finger[i]
        return self

    def join(self, n1):
        if self == n1:
            for i in range(k):
                self.finger[i] = self
            self.predecessor = self
        else:
            self.init_finger_table(n1)
            self.update_others()
            # Move keys !!!

    def init_finger_table(self, n1):
        self.finger[0] = n1.find_successor(self.start[0])
        self.predecessor = self.successor().predecessor
        self.successor().predecessor = self
        self.predecessor.finger[0] = self
        for i in range(k - 1):
            if Ebetween(self.start[i + 1], self.id, self.finger[i].id):
                self.finger[i + 1] = self.finger[i]
            else:
                self.finger[i + 1] = n1.find_successor(self.start[i + 1])

    def update_others(self):
        for i in range(k):
            prev = decr(self.id, 2 ** i)
            p = self.find_predecessor(prev)
            if prev == p.successor().id:
                p = p.successor()
            p.update_finger_table(self, i)

    def update_finger_table(self, s, i):
        if Ebetween(s.id, self.id, self.finger[i].id) and self.id != s.id:
            self.finger[i] = s
            p = self.predecessor
            p.update_finger_table(s, i)

    # def update_others_leave(self):
    #     for i in range(k):
    #         prev = decr(self.id, 2 ** i)
    #         p = self.find_predecessor(prev)
    #         p.update_finger_table(self.successor(), i)
    #
    # # not checked
    # def leave(self):
    #     self.successor().predecessor = self.predecessor
    #     self.predecessor.setSuccessor(self.successor())
    #     self.update_others_leave()
    #
    # def setSuccessor(self, succ):
    #     self.finger[0] = succ

    def leave(self):
        self.successor().predecessor = self.predecessor
        self.update_leave_others(self.successor())
        self.predecessor.finger[0] = self.finger[0]

    def update_leave_others(self, x):
        for i in range(k):
            prev = decr(self.id, 2 ** i)
            p = self.find_predecessor(prev)
            if prev == p.successor().id:
                p = p.successor()
            p.update_leave_finger_table(self, i, x)

    def update_leave_finger_table(self, s, i, x):
        if self.finger[i].id == s.id:
            self.finger[i] = x
            p = self.predecessor
            p.update_leave_finger_table(s, i, x)


# def hash(line):
#     import sha
#     key = long(sha.new(line).hexdigest(), 16)
#     return key
#
#
# def id():
#     return long(random.uniform(0, 2 ** k))


def printNodes(node):
    print(' Ring nodes:')
    end = node
    print(node.id)
    while end != node.successor():
        node = node.successor()
        print(node.id)
    print('-----------')


def showFinger(node):
    print('Finger table of node ' + str(node.id))
    print('start:node')
    for i in range(k):
        print(str(node.start[i]) + ' : ' + str(node.finger[i].id))
    print('-----------')


n1 = Node(32)
n1.join(n1)

n2 = Node(40)
n2.join(n1)

n3 = Node(52)
n3.join(n1)

n4 = Node(60)
n5 = Node(70)
n6 = Node(79)
n7 = Node(80)
n8 = Node(85)
n9 = Node(102)
n10 = Node(113)
n11 = Node(114)
#
n4.join(n1)
n5.join(n1)
n6.join(n1)
n7.join(n1)
n8.join(n1)
n9.join(n1)
n10.join(n1)
n11.join(n1)
#
# showFinger(n1)
# showFinger(n5)
# showFinger(n6)
# showFinger(n7)
# showFinger(n8)
# showFinger(n9)
# showFinger(n10)
# showFinger(n11)

n11.leave()
n10.leave()
n9.leave()
n8.leave()
# n7.leave()
# n6.leave()
# n5.leave()
# n4.leave()
# n3.leave()
# n2.leave()
# n1.leave()
print('---------------')

showFinger(n1)
showFinger(n2)
showFinger(n3)
showFinger(n4)
showFinger(n5)
showFinger(n6)
showFinger(n7)
# showFinger(n8)
# showFinger(n9)
# showFinger(n10)

#
# printNodes(n2)
