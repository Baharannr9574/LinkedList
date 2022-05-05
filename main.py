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


listOne = LinkedList()
listOne.headValue = Node("first")
e2 = Node("Two")
e3 = Node("Three")

listOne.headValue.nextValue = e2

e2.nextValue = e3

listOne.listprint()

listTwo = LinkedList()
listOne.headValue = Node("four")
e4 = Node("Five")
e5 = Node("Six")

listOne.headValue.nextValue = e4

e4.nextValue = e5

listTwo.listprint()
