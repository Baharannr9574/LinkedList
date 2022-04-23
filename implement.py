from main import Node
from main import LinkedList

l1 = LinkedList()
l2 = LinkedList()

n1 = int(input('How many elements would you like to add? '))
for i in range(n1):
    data1 = int(input('Enter data item: '))
    l1.append(data1)



n2 = int(input('How many elements would you like to add? '))
for i in range(n2):
    data2 = int(input('Enter data item: '))
    l2.append(data2)


l1.display()
l2.display()




