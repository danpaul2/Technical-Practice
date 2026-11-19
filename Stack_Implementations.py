class ListStack:
     def __init__(self):
           self.__top = -1
           self.__stack = []
    

     def push(self,item):
          self.__top +=1
          self.__stack.append(item)
     
     
     def pop(self):
          if self.__top == -1:
               raise IndexError("Stack is empty")
          
         
          pop = self.__stack[self.__top]
          self.__stack.pop()
          self.__top -=1
          return pop 
     
     def peek(self):
          if self.__top ==-1:
            raise IndexError("Stack is empty")

          return self.__stack[self.__top]

     def traversal(self):
          if self.__top == -1:
               return 
          for i in range(self.__top,-1,-1):
               print(self.__stack[i])



class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedListStack:
    def __init__(self):
        self.__head = None 

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.__head
        self.__head = newNode 
        

    def pop(self):
        if not self.__head:
            return 
        popped = self.__head.data
        self.__head = self.__head.next 
        return popped
        

    def display(self):
        if not self.__head:
            return 
        temp = self.__head 
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next 
        print('None')
        
    def peek(self):
        if not self.__head:
            return 
        return self.__head.data 




if __name__ == "__main__":
    print("Stack implemented using Linked List:")
    s1 = LinkedListStack()
    s1.push(5)
    s1.push(2)
    s1.push(8)
    print(s1.peek())
    print()
    s1.display()
    print()
    s1.pop()
    print(s1.peek())
    print()

    print("Stack implemented using List:")
    s2 = ListStack()
    s2.push(1)
    print(s2.peek())
    print()
    s2.push(2)
    s2.traversal()
    print()
    s2.peek()
    s2.pop()
    s2.peek()
         
    
              
