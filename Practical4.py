#3005 Shravan
class Array_Q:
   DEFAULT_CAPACITY = 10         

def __init__(self):
    self._data = [None] 
    self._size = 0
    self._front = 0
    self._back = 0

def __len__(self):
    return self._size

def is_empty(self):
    return self._size == 0

def first(self):
    if self.is_empty():
        raise Empty('Queue is empty')
    return self._data[self._front]
    

def dequeueStart(self):
    if self.is_empty():
        raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None        
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    self._back = (self._front + self._size - 1) % len(self._data)
    return answer
    
def dequeueEnd(self):
    if self.is_empty():
        raise Empty('Queue is empty')
    back = (self._front + self._size - 1) % len(self._data)
    answer = self._data[back]
    self._data[back] = None         
    self._front = self._front
    self._size -= 1
    self._back = (self._front + self._size - 1) % len(self._data)
    return answer

def enqueueEnd(self, e):
    if self._size == len(self._data):
        self._resize(2 * len(self.data))     
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1
    self._back = (self._front + self._size - 1) % len(self._data)
        
def enqueueStart(self, e):
    if self._size == len(self._data):
        self._resize(2 * len(self._data))     
    self._front = (self._front - 1) % len(self._data)
    avail = (self._front + self._size) % len(self._data)
    self._data[self._front] = e
    self._size += 1
    self._back = (self._front + self._size - 1) % len(self._data)

def _resize(self, cap):                 
    old = self._data                       
    self._data = [None] * cap              
    walk = self._front
    for k in range(self._size):           
        self._data[k] = old[walk]            
        walk = (1 + walk) % len(old)         
    self._front = 0                          
    self._back = (self._front + self._size - 1) % len(self._data)
        
queue = Array_Q()
queue.enqueueEnd(1)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue._data
queue.enqueueEnd(2)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue._data
queue.dequeueStart()
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueueEnd(3)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueueEnd(4)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.dequeueStart()
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueueStart(5)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.dequeueEnd()
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
queue.enqueueEnd(6)
print(f"1st Element: {queue._data[queue._front]}, Last Element: {queue._data[queue._back]}")
