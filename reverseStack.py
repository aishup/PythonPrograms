from collections import deque


class ReverseStr:
    def __init__(self):
        self.container = deque()
        
    def stackAppend(self,paragraph):

        for char in paragraph:
            self.container.append(char)

        return self.container

def reverse_string(s):

    strStack = ReverseStr()
    strStack.stackAppend(s)
    #print(len(strStack.container))
    output =""
    while len(strStack.container) != 0:
        output += strStack.container.pop()
    print(output)

if __name__ == "__main__":

    
    a = "takes 1"
    reverse_string(a) 

    #should return "91-DIVOC ereuqnoc lliw eW"