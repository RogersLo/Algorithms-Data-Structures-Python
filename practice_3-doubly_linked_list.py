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
            

if __name__ == "__main__":
    
    LinkedList = DoublyLinkedList()
    LinkedList.append(1)
    LinkedList.append(2)
    LinkedList.append(3)
    LinkedList.prepend(5)
    LinkedList.prepend(77)
    LinkedList.print_linkedlist()

    