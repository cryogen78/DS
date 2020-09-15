# To store the elements in 1-D array and provide an option to perform the operations like searching, sorting, merging, reversing the elements.
# 3005 Shravan
class List:
    def __init__(self, lst):
        self.lst = lst

    def linear_search(self, ele):
        for i in range(len(self.lst)):
            if self.lst[i] == ele:
                return i
        return False

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

    def merge(self, lst_2):
        merged_lst = self.lst.copy()
        for e in lst_2:
            merged_lst.append(e)
        return merged_lst

    def reverse(self):
        reversed_lst = []
        for i in reversed(range(0, len(self.lst))):
            reversed_lst.append(self.lst[i])
        return reversed_lst


if __name__ == "__main__":
    test_list = [35, 10, 43, 82, 66, 51, 97]
    test_list_2 = [11, 36, 44, 52, 67, 83, 98]
    test_value_1 = 43
    test_value_2 = 44
    object_1 = ListOperations(test_list)
    object_2 = ListOperations(test_list)
    
    
    linear_result_1 = object_1.linear_search(test_value_1)
    print(linear_result_1)
    linear_result_2 = object_2.linear_search(test_value_2)
    print(linear_result_2)
    bubble_sort = object_1.bubble_sort()
    print(bubble_sort)
    selection_sort = object_1.selection_sort()
    print(selection_sort)
    insertion_sort = object_1.insertion_sort()
    print(insertion_sort)
    merge = object_1.merge(test_list_2)
    print(merge)
    reverse = object_1.reverse()
    print(reverse)

