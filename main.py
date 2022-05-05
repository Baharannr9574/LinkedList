class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(Node):
    def __init__(self,data):
        Node.__init__(self, data)
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



def addTwoNumbers(l1:LinkedList, l2:LinkedList):
    dummy = cur = Node(0)
    carry = 0
    while l1 or l2 or carry:
         print(l1.data)
         print(l2.data)
         print(carry)