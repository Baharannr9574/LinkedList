from main2 import Node, LinkedList, addTwoNumbers,addTwoNumbersV2

list1 = LinkedList()
list2 = LinkedList()

# n1 = int(input('How many elements would you like to add? '))
# for i in range(n1):
# data1 = int(input('Enter data item: '))

list1.append(3)

# n2 = int(input('How many elements would you like to add? '))
# for i in range(n2):
# data2 = int(input('Enter data item: '))

list2.append(4)

print(addTwoNumbers(list1.head, list2.head))

print(addTwoNumbersV2(list1, list2))
