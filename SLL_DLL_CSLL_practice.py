class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def length(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next 
        return count 

    def insertAtFront(self,data):
        newNode = Node(data)
        newNode.next = self.head 
        self.head = newNode 

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
            return 

        current = self.head 
        while current.next:
            current = current.next 
        current.next = newNode 

    def insertAtIndex(self,index,data):
        newNode = Node(data)
        if index<0:
            raise IndexError("Index out of bounds")
        if index==0:
            self.insertAtFront(data)
            return 

        current = self.head 
        current_index = 0
        while current and current_index <index-1:
            current = current.next 
            current_index +=1 

        if current is None:
            raise IndexError("Index out of bounds")

        newNode.next = current.next 
        current.next = newNode 

    def deleteAtFront(self):
        if self.head is None:
            return 
        self.head = self.head.next 

    def deleteAtEnd(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
        
        current = self.head
        while current.next.next:
            current = current.next 
        current.next = None 

    def deleteAtIndex(self,index):
        if self.head is None:
            return 
        
        if index==0:
            self.deleteAtFront()
            return  

        current = self.head 
        current_index = 0

        while current and current_index < index -1:
            current = current.next 
            current_index += 1
        
        if current is None or current.next is None:
            raise IndexError("Index out of bounds")
        
        current.next = current.next.next

  

    def show(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next 
        print("None")

    def reversal(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node
        self.head = prev 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def length(self):
        count = 0 
        current = self.head 
        while current:
            count+=1
            current = current.next 
        return count 

    def insertAtFront(self,data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode 
        self.head = newNode 

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode 
        newNode.prev = current 

    def insertAtIndex(self,index,data):
        newNode = Node(data)
        if index<0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insertAtFront(data)
            return 
        current = self.head 
        current_index = 0
        while current and current_index < index-1:
            current = current.next 
            current_index +=1
        if current is None:
            raise IndexError("Index out of bounds")
        newNode.next = current.next 
        newNode.prev = current   

        if current.next is not None:
            current.next.prev = newNode
        current.next = newNode 

    def deleteAtFront(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
        
        self.head = self.head.next 
        self.head.prev = None 
    
    def deleteAtEnd(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 

        current = self.head 
        while current.next:
            current = current.next 
        current.prev.next = None 

    def deleteAtIndex(self,index):
        if index<0 or self.head is None:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.deleteAtFront()
            return 
        current = self.head 
        current_index = 0

        while current and current_index < index:
            current = current.next 
            current_index += 1

        if current is None:
            raise IndexError("Index out of bounds")
        if current.next is None:
            self.deleteAtEnd()
            return 

        current.prev.next = current.next 
        current.next.prev = current.prev 

    def reversal(self):
        if self.head is None or self.head.next is None:
            return 

        current = self.head 
        temp = None 

        while current is not None:
            temp = current.prev 
            current.prev = current.next 
            current.next = temp 

            current = current.prev 
        if temp is not None:
            self.head = temp.prev

    def show(self):
        if self.head is None:
            print("The Doubly linked list is empty")
            return 
        current = self.head 
        tail = None 
        while current:
            print(current.data,end = " -> ")
            current = current.next 
        print("None")


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None 

    def length(self):
        if self.head is None:
            return 0
        count = 0 
        current = self.head 
        while True:
            count+=1
            current = current.next 
            if current == self.head:
                break 
        return count

    def insertAtFront(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
            newNode.next = self.head 
            return 

        current = self.head 
        while current.next != self.head:
            current = current.next 

        newNode.next = self.head 
        current.next = newNode
        self.head = newNode 

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode 
            newNode.next = self.head 
            return 

        current = self.head 
        while current.next !=self.head:
            current = current.next 

        current.next = newNode 
        newNode.next = self.head 

    def insertAtIndex(self,index,data):
        if index<0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insertAtFront(data)
            return 

        current = self.head 
        current_index = 0

        while current_index < index-1:
            current = current.next 
            current_index +=1
            if current==self.head:
                raise IndexError("Index out of bounds")

        newNode = Node(data)
        newNode.next = current.next 
        current.next = newNode

    def deleteAtFront(self):
        if self.head is None:
            return 

        if self.head.next == self.head:
            self.head = None 
            return 

        current = self.head 
        while current.next !=self.head:
            current = current.next 

        current.next = self.head.next 
        self.head = self.head.next 

    def deleteAtEnd(self):
        if self.head is None:
            return 
        if self.head.next == self.head:
            self.head = None 
            return 
        current = self.head 
        while current.next.next != self.head:
            current = current.next 
        current.next = self.head 

    def deleteAtIndex(self,index):
        if index<0 or self.head is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.deleteAtFront()
            return 

        current = self.head 
        current_index = 0

        while current_index < index -1:
            current = current.next 
            current_index +=1 
            if current == self.head:
                raise IndexError("Index out of bounds")
            
        
        
        if current.next.next == self.head:
            self.deleteAtEnd()
            return 
        
        current.next = current.next.next 

    def reversal(self):
        if self.head is None or self.head.next == self.head:
            return 

        prev = None
        current = self.head 
        next_node = None

        while True:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 
            if current == self.head:
                break 

        self.head.next = prev
        self.head = prev 

    def show(self):
        if self.head is None:
            print("The Circular linked list is empty")
            return
        current = self.head 
        while True:
            print(current.data,end =" -> ")
            current = current.next 
            if current == self.head:
                break 
        print("[Head]")




            

        


         

if __name__ == '__main__':
    print("Singly Linked List Operations:")
    obj = SinglyLinkedList()
    obj.insertAtFront(10)
    obj.insertAtEnd(20)
    obj.show()
    obj.insertAtIndex(1,30)
    obj.show()
    obj.insertAtEnd(45)
    obj.show()
    obj.reversal()
    obj.show()
    obj.deleteAtIndex(2)
    obj.show()
    obj.deleteAtEnd()
    obj.show()
    obj.deleteAtFront()
    obj.show()
    print("")
    print("Doubly Linked List Operations:")
    obj_dll = DoublyLinkedList()
    obj_dll.insertAtFront(10)
    obj_dll.insertAtEnd(20)
    obj_dll.show()
    obj_dll.insertAtIndex(1,30)
    obj_dll.show()
    obj_dll.insertAtEnd(45)
    obj_dll.show()
    obj_dll.reversal()
    obj_dll.show()
    obj_dll.deleteAtIndex(2)
    obj_dll.show()
    obj_dll.deleteAtEnd()
    obj_dll.show()
    obj_dll.deleteAtFront()
    obj_dll.show()

    print("")
    print("Circular Singly Linked List Operations:")
    obj_cll = CircularSinglyLinkedList()
    obj_cll.insertAtFront(40)
    obj_cll.insertAtEnd(50)
    obj_cll.show()
    obj_cll.insertAtIndex(1,35)
    obj_cll.show()
    obj_cll.reversal()
    obj_cll.show()
    obj_cll.deleteAtIndex(2)
    obj_cll.show()
    obj_cll.deleteAtEnd()
    obj_cll.show()
    obj_cll.deleteAtFront()
    obj_cll.show()








        

    

            


