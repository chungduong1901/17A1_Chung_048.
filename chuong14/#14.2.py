#14.2
class InputError(Exception):
    pass

def nhap_so_nguyen_duong():
    while True:
        try:
            so_nguyen = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            
            if so_nguyen == 0:
                break  # Kết thúc khi nhập 0
            
            if so_nguyen < 0:
                raise InputError("Lỗi: Số không được là số nguyên âm.")
            
            if 'prev_input' in locals() and so_nguyen == prev_input:
                raise InputError("Lỗi: Bạn đã nhập 4 số nguyên dương giống nhau liên tiếp.")
            
            prev_input = so_nguyen
            
            print("Nhập thành công:", so_nguyen)

        except ValueError:
            print("Lỗi: Bạn đã nhập một chuỗi không phải số nguyên.")
        
        except InputError as ie:
            print(ie)

if __name__ == "__main__":
    nhap_so_nguyen_duong()