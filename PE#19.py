# Implement a slice method for the UnorderedList class. 
# It should take two parameters, start and stop, and return a copy of the list starting at the start position 
# and going up to but not including the stop position.

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

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def slice(self, start, stop):
        x = 0
        token = self.head
        SlicedList = UnorderedList()
        while x < stop:
            if x >= start:
                SlicedList.add(token.data)
                token = token.getNext()
                x += 1
                
                if token == None:
                    x = stop
            else:
                token = token.getNext()
                x += 1
         
        return SlicedList.reverse()

    def reverse(self):
        current = self.head
        reversedlist = UnorderedList()
        while current != None:
            reversedlist.add(current.data)
            current = current.getNext()

        return reversedlist

    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
        
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def pop(self):
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
        
                
            
            
