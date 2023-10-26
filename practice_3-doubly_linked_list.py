# pre and next是出現在node中的屬性不是LinkedList的屬性
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def print_linkedlist(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end="")
            tmp = tmp.next
            if tmp:
                print(" <-> ", end="")
        
                     
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            

# pop & pop_first的邏輯都是先分成三種case: 1.空 2.只有一個元素 3. 兩個元素及以上 

    def pop_first(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        
        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        # tmp = None
        return
        
    def pop(self):
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        
        tmp = self.tail
        self.tail = tmp.prev
        self.tail.next = None
        tmp.prev = None
        return
        
        
        
if __name__ == "__main__":
    
    LinkedList = DoublyLinkedList()
    LinkedList.append(1)
    LinkedList.append(2)
    LinkedList.append(3)
    LinkedList.prepend(5)
    LinkedList.prepend(77)
    LinkedList.pop()

    # LinkedList.pop_first()
    LinkedList.print_linkedlist()

    