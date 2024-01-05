def party_late(arrivals, name):
    index = arrivals.index(name)
    if index < len(arrivals) / 2 and index != len(arrivals) - 1:
        return True
    else:
        return False

arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(party_late(arrivals, 'Gilbert'))  
print(party_late(arrivals, 'Ford'))
print(party_late(arrivals, 'Mona'))  
