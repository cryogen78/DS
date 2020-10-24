#3005 (New Rollno:372) Shravan SYIT
#To create a Stack For implementation of Array.
class Stack_5:
     def __init__(self):
         self.container = []  

     def isEmpty(self):
         return self.size() == 0   

     def push(self, item):
         self.container.append(item)  

     def pop(self):
         return self.container.pop()    

     def size(self):
         return len(self.container)  

     def show(self):
         return self.container 

s = Stack_5()
s.push('1')
s.push('2')
s.push('5')
s.push('3')
s.push('4')
print(s.pop())
print(s.show())
