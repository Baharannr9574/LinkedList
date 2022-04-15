class Node:
      def __init__(self,data):
        self.data = data
        self.next = None



class Linkedlist:
      def __init__(self):
         self.head = None

      def listprint(self):
          node = self.head
          nodes = []
          while node is not None:
              nodes.append(node.data)
              node = node.next
          print(nodes)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

l = Linkedlist()
l.head = node1
node1.next = node2
node2.next = node3


l.listprint()