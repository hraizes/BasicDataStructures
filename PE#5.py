#5: Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.

class QueueX:

    def __init__(self): #constructor 
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item): #add item to the rear (last index)
        self.items.append(item)

    def dequeue(self): #remove item from the front (first index) 
        return self.items.pop(0)

    def size(self): 
        return len(self.items)






