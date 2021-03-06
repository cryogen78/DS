# To store the elements in 1-D array and provide an option to perform the operations like searching, sorting, merging, reversing the elements.
#3005 (New Rollno:372) Shravan SYIT
class Array:
            
    def linear_search(self,lst,n):
        for i in range(len(lst)):
            if lst[i] == n:
                return f'Position :{i}'
        return -1
    
    def insertion_sort(self,lst):
        for i in range(len(lst)):
            
            index = lst[i]
            
            k = i - 1
            
            while k >= 0 and lst[k] > index:
                lst[k + 1] = lst[k]
                k -= 1
                
            lst[k+1]  = index
            
        return lst
    
    def merge(self,lst1,lst2):
        return Array.insertion_sort(lst1 + lst2)
    
    def reverse(self,lst):
        return lst[::-1]

lst = [5,31,44,94,108,109]
Arrmod = Array()
print(Arrmod.linear_search(lst,3))
