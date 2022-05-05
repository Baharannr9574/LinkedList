class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextValue = None


class LinkedList:
    def __init__(self):
        self.headValue = None

    def listprint(self):
        printval = self.headValue
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextValue


def merge(List_1, List_2):
    head_ptr = temp_ptr = Node()  

    while List_1 or List_2:

        if List_1 and List_2:
            temp_ptr.nextValue = Node(List_1.dataval)
            List_1 = List_1.nextValue
            print(List_1.dataval + List_2.dataval)

        else:
            temp_ptr.nextValue = Node(List_2.dataval)
            List_2 = List_2.nextValue
            print(List_1.dataval + List_2.dataval)

        temp_ptr = temp_ptr.nextValue


listOne = LinkedList()
listOne.headValue = Node("first")
e2 = Node("Two")
e3 = Node("Three")

listOne.headValue.nextValue = e2

e2.nextValue = e3

listOne.listprint()

listTwo = LinkedList()
listTwo.headValue = Node("four")
e4 = Node("Five")
e5 = Node("Six")

listTwo.headValue.nextValue = e4

e4.nextValue = e5

listTwo.listprint()

merge(listOne.headValue, listTwo.headValue)
