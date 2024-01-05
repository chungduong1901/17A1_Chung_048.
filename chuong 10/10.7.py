def process_string(s, s_sub, s_find, s_replace):
    # In chuỗi s
    print("Chuỗi s ban đầu:", s)
    
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    s = s.strip()
    print("Chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối:", s)
    
    # In chuỗi với ký tự đầu chuỗi viết hoa
    print("Chuỗi với ký tự đầu chuỗi viết hoa:", s.capitalize())
    
    # Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
    count = s.count(s_sub)
    print("Số lần chuỗi con s_sub xuất hiện trong chuỗi s:", count)
    
    # Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau tìm kiếm và thay thế
    replaced_string = s.replace(s_find, s_replace)
    print("Chuỗi sau khi tìm kiếm và thay thế:", replaced_string)

# Nhập chuỗi s, chuỗi con s_sub, chuỗi tìm kiếm s_find, chuỗi thay thế s_replace
s = input("Nhập chuỗi s: ")
s_sub = input("Nhập chuỗi con s_sub: ")
s_find = input("Nhập chuỗi tìm kiếm s_find: ")
s_replace = input("Nhập chuỗi thay thế s_replace: ")

# Gọi hàm xử lý chuỗi
process_string(s, s_sub, s_find, s_replace)
