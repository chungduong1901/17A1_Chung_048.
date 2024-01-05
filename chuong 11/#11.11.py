#11.11
def process_tuple(tup, pos_index, neg_index, s_find):
    print("Tuple:", tup)
    print("Tuple[{}]={}".format(pos_index, tup[pos_index]))
    print("Tuple[{}]={}".format(neg_index, tup[neg_index]))
    count = tup.count(s_find)
    print("{} xuất hiện trong tuple {} lần".format(s_find, count))

t = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')
pos = 2
neg = -2
search_str = 'blue'
process_tuple(t, pos, neg, search_str)
