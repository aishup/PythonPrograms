from pip import main


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def _init_(self):
        self.head = None
    def insert_at_begining(self,data):
        node = Node(data,self.Head)
        self.head = node  
    def printLL(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        lListstr = " "
        while  itr:
            lListstr += itr + "-->"
            itr = itr.next
        print(lListstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.printLL()


        
