class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def append(self, data):
        if self.last_node is None:
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


    def getsize(self):
        count = 0
        node = self.head
        while (node != None):
            count += 1
            node = node.next
        print(count)




def addTwoNumbers(l1:LinkedList, l2:LinkedList):
    carry = 0
    while l1 or l2:
        if l1:
            carry += l1.data
            l1 = l1.next
        if l2:
            carry += l2.data
            l2 = l2.next

    return carry


