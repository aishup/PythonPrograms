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

    def print(self):

        if self.Head is None:
            print("Linked List is empty")
            return
        
        itr = self.Head
        Llstr = ""
        while itr:
            Llstr = str(itr.data) + " " + "--->"
            itr = itr.next 
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.print()