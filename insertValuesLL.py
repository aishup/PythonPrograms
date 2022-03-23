class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertValues(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
            
    def insert_at_end(self,data):
        if self.head == None:
            node = Node(data,self.head)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)     
    
    def print(self):
        if self.head == None:
            print("Linked List is empty")
        
        itr = self.head
        LLstr = ""
        while itr:
            LLstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(LLstr)

ll = LinkedList()
ll.insertValues([3,4])
ll.print()


