class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    
    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        
        itr = self.head
        LLstr = " "

        while itr:
            LLstr += str(itr.data) + " -->"
            itr = itr.next
        
        print(LLstr)

ll = LinkedList()
#ll.insert_at_beginning(10)
#ll.insert_at_beginning(20)
ll.insert_at_end(15)
ll.insert_at_end(35)
ll.print()
        