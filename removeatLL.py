class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.Head = None
    
    def insert_at_beginning(self,data):
        
        node = Node(data,self.Head)
        self.Head = node

    def insert_at_end(self,data):
        if self.Head == None:
            self.insert_at_beginning(data)
            return
        
        itr = self.Head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def get_length(self):
        count = 0
        if self.Head != None:
            itr = self.Head
            while itr:
                count+=1
                itr = itr.next
        return count            

    def removeat(self,index):
        if self.Head == None:
            return
        if index<0 or index >= self.get_length():
            raise Exception("Invalid Index")
            return
        count = 0
        itr = self.Head
        while itr:
            if index == count + 1:
                itr.next = itr.next.next
                return
            count+=1
            itr = itr.next
    
    def print(self):
        if self.Head == None:
            print("Linked List is empty")
            return
        
        itr = self.Head
        LLstr = ""
        while itr:
            LLstr += str(itr.data) + "-->"
            itr = itr.next
        print(LLstr)

ll = LinkedList()

ll.insert_at_beginning("0-violet")
ll.insert_at_end("1-indigo")
ll.insert_at_end("2-blue")
ll.insert_at_end("3-grey")
ll.insert_at_end("4-indigo")
ll.insert_at_end("5-yellow")
ll.print()
ll.removeat(6)
ll.print()


        





