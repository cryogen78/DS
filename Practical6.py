#to sort a list of elements. Give user the option to perform sorting using Insertion sort, Bubble sort or Selection sort.
#3005 (New Rollno:372) Shravan SYIT
class Sort:
    def __init__(self, lst):
        self.lst = lst

    def bubble_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(len(sorted_lst) - 1):
            for j in range(0, len(sorted_lst) - i - 1):
                if sorted_lst[j] > sorted_lst[j + 1]:
                    sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
        return sorted_lst

    def selection_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(len(sorted_lst)):
            min_idx = i
            for j in range(i + 1, len(sorted_lst)):
                if sorted_lst[min_idx] > sorted_lst[j]:
                    min_idx = j
            sorted_lst[i], sorted_lst[min_idx] = sorted_lst[min_idx], sorted_lst[i]
        return sorted_lst

    def insertion_sort(self):
        sorted_lst = self.lst.copy()
        for i in range(1, len(sorted_lst)):
            key = sorted_lst[i]
            j = i - 1
            while j >= 0 and key < sorted_lst[j]:
                sorted_lst[j + 1] = sorted_lst[j]
                j -= 1
            sorted_lst[j + 1] = key
        return sorted_lst


if __name__ == '__main__':
    test_list = [44,31,108,94,109]
    test_sort = Sort(test_list)
    print(test_sort.bubble_sort())
    print(test_sort.selection_sort())
    print(test_sort.insertion_sort())
