
def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2

def multiply_tuple(my_tuple, n):
    return my_tuple * n

def find_index_in_tuple(my_tuple, x, start=None, end=None):
    try:
        return my_tuple.index(x, start, end)
    except ValueError:
        return -1

def count_occurrences_in_tuple(my_tuple, x):
    return my_tuple.count(x)

def convert_to_list(my_tuple):
    return list(my_tuple)

def convert_to_tuple(my_list):
    return tuple(my_list)
