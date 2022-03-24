class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.Head = None
    
    def insert_in_between(self,data,index):
        if self.Head == None:
            print("Linked List is empty")
        if index == 1:
                    



