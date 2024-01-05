# list_operations.py

def append_element(my_list, x):
    my_list.append(x)

def extend_list(list1, list2):
    list1.extend(list2)

def insert_element(my_list, i, x):
    my_list.insert(i, x)

def remove_element(my_list, x):
    my_list.remove(x)

def pop_element(my_list, i=None):
    return my_list.pop(i)

def find_index(my_list, x, start=None, end=None):
    return my_list.index(x, start, end)

def count_occurrences(my_list, x):
    return my_list.count(x)

def sort_list(my_list, key=None, reverse=False):
    my_list.sort(key=key, reverse=reverse)

def reverse_list(my_list):
    my_list.reverse()

def copy_list(original_list):
    return original_list.copy()
