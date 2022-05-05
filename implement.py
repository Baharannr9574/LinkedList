from main import Node,LinkedList,addTwoNumbers


list1 = LinkedList()
list2 = LinkedList()


n1 = int(input('How many elements would you like to add? '))
for i in range(n1):
    data1 = int(input('Enter data item: '))
    list1.append(data1)



n2 = int(input('How many elements would you like to add? '))
for i in range(n2):
    data2 = int(input('Enter data item: '))
    list2.append(data2)



#nodegenrator1 = l1.traverse()
#for i in nodegenrator1:
   # print(i)

addTwoNumbers(list1,list2)