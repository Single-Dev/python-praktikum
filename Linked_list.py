
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


llist = LinkedList()

llist.head = Node('Dushanba')
tuesday = Node('Seashanba')
wednasday = Node('Chorshanba')

llist.head.next = tuesday
tuesday.next = wednasday
print(llist.head.data)
print(llist.head.next.data)
print(llist.head.next.next.data)