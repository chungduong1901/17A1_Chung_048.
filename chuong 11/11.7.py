def elementwise_greater_than(L, thresh):
    result = [x > thresh for x in L]
    return result

L = [1, 2, 3, 4]
thresh = 2
print(elementwise_greater_than(L, thresh)) 
