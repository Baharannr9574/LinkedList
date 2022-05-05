from main import Node, LinkedList

list1 = LinkedList()
list2 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


list1.head.next = e2

e2.next = e3

list1.listprint()
