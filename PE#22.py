#Implement a stack using linked lists

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

class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, item): 
        temp = Node(item) #creates a new node
        temp.setNext(self.head) 
        self.head = temp #added item becomes head of link list

    def pop(self):
        if self.isEmpty() == False: #list is not empty
            removed = self.head.data #top value of stack 
            self.head = self.head.next #new top
            return removed #return popped value
        else:
            print("Empty Stack")

    def peek(self):
        return self.head.data #returns top value

    def size(self):
        var = self.head #starting node
        count = 0
        while var != None: #counts nodes until last one is reached 
            count += 1
            var = var.getNext()
        return count
        

