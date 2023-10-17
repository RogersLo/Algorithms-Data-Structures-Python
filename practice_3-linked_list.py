class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print_linkedlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
            if tmp:
                print("->", end=" ")  
                
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node  
            
    def pop_first(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        
        tmp = self.head
        self.head = tmp.next
        tmp = None
        return tmp       
            
    def pop(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

       
            
            
            
if __name__ == "__main__":
    Linkedlist = Linkedlist()
    Linkedlist.append(1)
    Linkedlist.append(2)
    Linkedlist.append(3)
    Linkedlist.print_linkedlist()
    print("\n====== Start prepend ======")
    Linkedlist.prepend(7)
    Linkedlist.prepend(8)
    Linkedlist.prepend(9)
    Linkedlist.print_linkedlist()
    print("\n====== Start pop first multiple times ======")
    Linkedlist.pop_first()
    Linkedlist.pop_first()
    Linkedlist.print_linkedlist()
    print("\n====== Start pop multiple times ======")
    # Linkedlist.pop()
    Linkedlist.print_linkedlist()

    