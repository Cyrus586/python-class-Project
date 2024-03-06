class ListOperations():
    @staticmethod
    def add_element(lst, element):
        lst.append(element)
        return lst
    # helps in performing various operatins on a list
    @staticmethod
    def remove_element(lst, element):
        if element in lst:
            lst.remove(element)
        return lst
    
    @staticmethod
    def count_element(lst):
        return len(lst)

    @staticmethod
    def reverse_list(lst):
        return lst[::-1] 
    
    @staticmethod 
    def sort_list(lst):
        return sorted(lst)
    
    @staticmethod 
    def sum_elements(lst):
        return sum(lst) 
    
my_list = [1,2,3,4,5]

print("------------------------------------")
my_list = ListOperations.add_element(my_list, 6)
print("List after adding element: ", my_list)  

my_list = ListOperations.remove_element(my_list, 3)
print("List after removing element: ", my_list)  

print("Number of elements in the list: ", ListOperations.count_element(my_list))

print("Reversed List: ", ListOperations.reverse_list(my_list))

print("Sorted List: ", ListOperations.sort_list(my_list))

print("Sum of elements in the list: ", ListOperations.sum_elements(my_list))

print("--------------------------------------")


