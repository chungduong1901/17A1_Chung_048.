import re
def is_valid_zip_code(zip_code):
    pattern = r'^\d{6}$'  
    if re.match(pattern, zip_code):
        return True
    else:
        return False
zip_code = input("Nhập mã zip code: ")
if is_valid_zip_code(zip_code):
    print("Mã zip code hợp lệ.")
else:
    print("Mã zip code không hợp lệ.")
