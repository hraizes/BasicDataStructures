#3 binary search with recursion no slices
def binarySearchRecPtr(alist, item):
    return binarySearchRecPtrHelper(alist,item, 0, len(alist)-1)

def binarySearchRecPtrHelper(alist, item, left, right):
    if right < left:
        return False
    mid = (left + right) // 2
    if (alist[mid] == item):
        return True
    elif item < alist[mid]:
        return binarySearchRecPtrHelper(alist, item, left, mid-1)
    else:
        return binarySearchRecPtrHelper(alist, item, mid+1, right)

class HashTable:
    def __init__(self, size = 11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0

    def put(self,key,data):
          
      hashvalue = self.hashfunction(key,self.length())
        
      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.count += 1
        if self.count == self.size:
            self.resize()
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue, self.length())
          while (self.slots[nextslot] != None) and (self.slots[nextslot] != key):
            nextslot = self.rehash(nextslot,self.length())

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
            self.count += 1
            if self.count == self.size:
                self.resize()
          else:
            self.data[nextslot] = data #replace

    def resize(self):
        newtable = HashTable((self.size*2))
        for i in range(self.length()):
            if self.slots[i] == None:
                i += 1
            else:
                key = self.slots[i]
                data = self.data[i]
                newtable.put(key, data)
                
        self.slots = newtable.slots
        self.data = newtable.data
        self.size = newtable.size
        self.count = newtable.count


    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

#quadric probing
    def rehash2(self,oldhash,probe,size):
        return (oldhash+probe**2)%size

    def get(self,key):
      startslot = self.hashfunction(key,self.length())

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,self.length())
           if position == startslot:
               stop = True
      return data

#6 implement the del method
    def delKey(self, key):
        hashvalue = self.hashfunction(key,self.length())

        if self.slots[hashvalue] == key:
            self.slots[hashvalue] = None
            self.data[hashvalue] = None
            self.count -= 1
        else:
            nextslot = self.rehash(hashvalue,length())
            while (self.slots[nextslot] != None) and (self.slots[nextslot] != key):
                nextslot = self.rehash(nextslot,self.length())

            if self.slots[nextslot] == None:
                print('Key does not exist')
            else:
                self.slots[nextslot] = None
                self.data[nextslot] = None
                self.count -= 1
                
#5 implement the in method 
    def isIn(self, key):
        startslot = self.hashfunction(key,self.length())

        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(position,self.length())
                if position == startslot:
                    stop = True

        return found
                

    def length(self):
        return self.size
                           
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __delitem__(self,key):
        self.delKey(key)

#4 implement the length function
    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self.isIn(key)


#16 implement the median of three method
def median(alist, first, last):
        middle = (first+last)//2
        pivot = last
        if alist[first] < alist[middle]:
            if alist[middle] < alist[last]:
                pivot = middle
            elif alist[last] < alist[first]:
                pivot = first

        return pivot

def quicksort(alist):
    if alist == []:
        return []
    else:
        if len(alist) > 2:
            pivotindex = median(alist, 0, len(alist)-1)
            pivotvalue = alist[pivotindex]
            alist[0], alist[pivotindex] = pivotvalue, alist[0]
        else:
            pivot = alist[0]

        rest = alist[1:]
        return (quicksort(ltfilter(rest, pivot)) +
                [pivot] +
                quicksort(gtfilter(rest, pivot)))
    
    def ltfilter(flist,pivot):
        result = []
        for value in flist:
            if value < pivot:
                result += [value]
            else:
                continue
        return result

    def gtfilter(flist, pivot):
        result = []
        for value in flist:
            if value >= pivot:
                result += [value]
            else:
                continue
        return result
