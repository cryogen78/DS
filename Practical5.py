#to search an element from a list and give user the option to perform Linear or Binary search. 
# 3005 Shravan
class Search :
    def __init__ ( self , list , element ) :
        self.list = list
        self.element = element

    def binary_search ( self ) :
        sorted_list = sorted ( self.list )
        start = 0
        end = len ( sorted_list ) - 1
        while start <= end :
            mid = (end + start) // 2
            if sorted_list [ mid ] < self.element :
                start = mid + 1
            elif sorted_list [ mid ] > self.element :
                end = mid - 1
            else :
                return mid
        return False

    def linear_search ( self ) :
        for i in range ( len ( self.list ) ) :
            if self.list [ i ] == self.element :
                return i
        return False


if __name__ == '__rollno__' :
    test_list = [ 31,94,44,108,5,16 ]
    testvalue_1 = 94
    testvalue_2 = 44
    test_search = Search ( test_list , testvalue_1 )
    print ( test_search.binary_search ( ) )
    print ( test_search.linear_search ( ) )
    testsearch_2 = Search ( test_list , testvalue_2 )
    print ( testsearch_2.binary_search ( ) )
    print ( testsearch_2.linear_search ( ) )

