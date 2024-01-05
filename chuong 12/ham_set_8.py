
def union_sets(set1, set2):
    return set1.union(set2)

def intersection_sets(set1, set2):
    return set1.intersection(set2)

def difference_sets(set1, set2):
    return set1.difference(set2)

def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

def add_element_to_set(set_, element):
    set_.add(element)

def remove_element_from_set(set_, element):
    set_.discard(element)

def is_subset(subset, superset):
    return subset.issubset(superset)

def is_superset(superset, subset):
    return superset.issuperset(subset)
