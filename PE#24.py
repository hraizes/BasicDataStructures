#Implement a Deque using a linked list

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

class Deque:

    def __init__(self):
        self.head = None

    def addFront(self, item):
        current = self.head 
        previous = None
        front = False
        while current != None and not front: #transerval to the front
            if current.getData() == None: #found front
                front = True
            else:
                previous = current 
                current = current.getNext()
                
        temp = Node(item) #new front item
        if previous == None: #no items in the list
            temp.setNext(self.head)
            self.head = temp
        else: 
            temp.setNext(None) #setting new front value to None
            previous.setNext(temp) #linking the old front to the new front

    def addRear(self, item): 
        temp = Node(item) #new rear item
        temp.setNext(self.head)
        self.head = temp       

    def removeFront(self):
        current = self.head
        previous = None
        end = False
        while not end:
            if self.isEmpty() == True:
                end = True
                print("Deque is Empty")
            elif self.size() == 1: #handles cases when there is only one item 
                end = True
                self.head = None
                return current.getData()
            elif current.getNext() == None: #reached the Front of the Queue
                end = True 
                previous.setNext(None) #sets the new front of the deck
                return current.getData() #returns the removed value
            else: #traversal to the front of the deque
                previous = current 
                current = current.getNext()

    def removeRear(self):
        if self.isEmpty() == False: #list is not empty
            removed = self.head.data #rear value of Deque 
            self.head = self.head.next #new rear
            return removed #return popped value
        else:
            print("Deque is Empty") 

    def isEmpty(self):
        return self.head == None

    def size(self):
        var = self.head #starting node
        count = 0
        while var != None: #counts nodes until last one is reached 
            count += 1
            var = var.getNext()
        return count
