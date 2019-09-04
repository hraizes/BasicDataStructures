class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#Implement a queue using linked lists

class Queue:
    
    def __init__(self):
        self.head = None

    def enqueue(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def dequeue(self): #traverse the linked list to the last node
        current = self.head
        previous = None
        end = False
        while not end:
            if self.size() == 1: #handles cases when there is only one item 
                end = True
                self.head = None #empty deque
                return current.getData()
            
            if current.getNext() == None: #reached the front of the Queue
                end = True 
                previous.setNext(None) #sets the new front of the deck
                return current.getData() #returns the dequeued value
            else: #traversal to the front of the Queue
                previous = current 
                current = current.getNext()
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        var = self.head #start
        count = 0
        while var != None:
            count += 1
            var = var.getNext()
        return count
