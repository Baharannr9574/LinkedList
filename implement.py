from main import Node,LinkedList,addTwoNumbers


list1 = LinkedList()
list2 = LinkedList()

list1.append(4)
list1.append(5)
list1.append(2)

list2.append(9)
list2.append(6)
list2.append(3)



#nodegenrator1 = l1.traverse()
#for i in nodegenrator1:
   # print(i)

print(list1.display())
print(list2.display())
print(addTwoNumbers(list1.head, list2.head))
