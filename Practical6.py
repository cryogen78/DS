#to sort a list of elements. Give user the option to perform sorting using Insertion sort, Bubble sort or Selection sort.
# 3005 Shravan
class Sort:
    def __init__(self, list):
        self.list = list

    def bubble_sort(self):
        sorted_list = self.list.copy()
        for i in range(len(sorted_list) - 1):
            for j in range(0, len(sorted_list) - i - 1):
                if sorted_list[j] > sorted_list[j + 1]:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    def selection_sort(self):
        sorted_list = self.list.copy()
        for i in range(len(sorted_list)):
            min_index = i
            for j in range(i + 1, len(sorted_lst)):
                if sorted_list[min_index] > sorted_list[j]:
                    min_index = j
            sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
        return sorted_list

    def insertion_sort(self):
        sorted_list = self.list.copy()
        for i in range(1, len(sorted_list)):
            key = sorted_list[i]
            j = i - 1
            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key
        return sorted_list


if __name__ == '__rollno__':
    test_list = [31,44,108,109,16,94,5]
    test_sort = Sort(test_list)
    print(test_sort.bubble_sort(test_sort))
    print(test_sort.selection_sort())
    print(test_sort.insertion_sort())

