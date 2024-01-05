# Tạo list các con thú
animals = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

# In ra list và số lượng thú
print("danh sách:", animals)
print("số đv:", len(animals))

# Nhập con thú cần tìm
search_animal = input("con cần tìm: ")

# Kiểm tra xem con thú cần tìm có trong list hay không
if search_animal in animals:
    print(search_animal, "có trong danh sách")
else:
    print(search_animal, "không có trong danh sách")
