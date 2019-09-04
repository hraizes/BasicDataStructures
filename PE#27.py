class Node2:

    def __init__(self, initdata):
        self.data = initdata
        self.back = None
        self.next = None
        
    def getBack(self):
        return self.back

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setBack(self, newback):
        self.back = newback

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class Head:

    def __init__(self):
        self.front = None 
        self.rear = None

class Deque2:

    def __init__(self):
        self.head = Head() #pointer to the

    def addFront(self, item):
        if self.isEmpty():
            self.addFirst(item)
        else:
            new_front = Node2(item)
            new_front.setBack(self.head.front)
            self.head.front.setNext(new_front)
            self.head.front = new_front
        
    def addRear(self, item):
        if self.isEmpty():
            self.addFirst(item)
        else:
            new_rear = Node2(item)
            new_rear.setNext(self.head.rear)
            self.head.rear.setBack(new_rear)
            self.head.rear = new_rear
        
    def addFirst(self, item):
        if self.isEmpty():
            first = Node2(item)
            self.head.front = first
            self.head.rear = first
        else:
            print("Deque is not empty")

    def removeRear(self):
        if self.size() == 1:
            self.removeAll()
            
        if self.isEmpty() == False: #list is not empty
            removed = self.head.rear.data
            self.head.rear = self.head.rear.next
            return removed
        else:
            print("Deque is Empty") #list is empty

    def removeFront(self):
        if self.size() == 1:
            self.removeAll()
            
        if self.isEmpty() == False:
            removed = self.head.front.data
            self.head.front = self.head.front.back
            return removed
        else:
            print("Deque is Empty")

    def removeAll(self):
        self.head.front = None
        self.head.rear = None
        
    def isEmpty(self):
        return (self.head.front and self.head.rear) == None

    def size(self):
        var = self.head.rear #starting node
        count = 0
        while var != None: #counts nodes until last one is reached
            count += 1
            var = var.getNext()
        return count

    def display(self):
        current = self.head.rear
        while current != None:
            print(current.getData(), end = ' ')
            current = current.getNext()

        
     


        
        
    
        
        
        

    

        
    

        

        
