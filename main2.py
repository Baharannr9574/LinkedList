class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Node.__init__(self, data)
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            # listOne.headValue = Node("first")
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        print(nodes)

    def traverse(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next


def addTwoNumbers(l1: LinkedList, l2: LinkedList):
    # dummy = cur = Node(0)
    carry = 0
    while l1 or l2:
        if l1:
            carry += l1.data
            l1 = l1.next
        if l2:
            carry += l2.data
            l2 = l2.next
        # cur.next = Node(carry % 10)
        # cur = cur.next
        # carry //= 10
    return carry


def addTwoNumbersV2(l1: LinkedList, l2: LinkedList):
    # dummy = cur = Node(0)
    carry = 0
    while l1.head or l2.head:
        if l1:
            currentNode = l1.head
            carry += currentNode.data
            l1.head=currentNode.next

        if l2:
            currentNode = l2.head
            carry += currentNode.data
            l2.head = currentNode.next


        # cur.next = Node(carry % 10)
        # cur = cur.next
        # carry //= 10
    return carry
