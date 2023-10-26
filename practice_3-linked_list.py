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
        # 一共分三種case，鍊表為空，鍊表只有一個元素，以及第三種情況
        
        # 鍊表為空
        if self.head == None:
            return
        
        # 鍊表只有一個元素
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        # 鍊表有兩個元素及以上
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        return tmp
    
    def pop(self):
        # 跟pop_first一樣，一共分三種case: 鍊表為空，鍊表只有一個元素，以及第三種情況 (大於等於兩個元素)
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        
        tmp = self.head
        while tmp.next.next: # 最後tmp指針會指在原本的tail前一個元素
            tmp = tmp.next
        
        tmp.next = None
        self.tail = tmp
        return tmp
           
                   
if __name__ == "__main__":
    print("\n====== Below is append area ======")
    Linkedlist = Linkedlist()
    Linkedlist.append(1)
    Linkedlist.append(2)
    Linkedlist.append(3)
    Linkedlist.print_linkedlist()
    print("\n====== Below is prepend area ======")
    Linkedlist.prepend(7)
    Linkedlist.prepend(8)
    Linkedlist.print_linkedlist()
    print("\n====== Below doing pop_first ======")
    Linkedlist.pop_first()
    Linkedlist.pop_first()
    Linkedlist.print_linkedlist()
    print("\n====== Below doing pop ======")
    Linkedlist.pop()
    Linkedlist.pop()
    Linkedlist.print_linkedlist()