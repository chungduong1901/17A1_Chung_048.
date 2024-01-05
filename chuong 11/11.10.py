def menu_is_boring(meals):
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

# Minh họa
print(menu_is_boring(['redneck ribs', 'prawn star ', 'san quentin squid','fist full of pizza ','honkey tonkl chicken']))  
print(menu_is_boring(['redneck ribs', 'prawn star', 'running bear salmon', 'running bear salmon','honkey tonkl chicken'])) 
