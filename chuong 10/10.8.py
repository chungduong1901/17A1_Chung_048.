import datetime

def xuly_ngay_thang():
    ngay = int(input("Nhập vào ngày: "))
    thang = int(input("Nhập vào tháng: "))
    nam = int(input("Nhập vào năm: "))

    try:
        ngay_thang_nam = datetime.date(nam, thang, ngay)
        print("Ngày theo định dạng ngày - tháng - năm:", ngay_thang_nam.strftime("%d - %m - %Y"))

        if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
            print("Năm nhập vào là năm nhuận.")
        else:
            print("Năm nhập vào không phải là năm nhuận.")

        thu_trong_tuan = ngay_thang_nam.strftime("%A")
        print("Ngày/tháng/năm nhập vào là thứ:", thu_trong_tuan)

        so_ngay_trong_thang = (datetime.date(nam, thang % 12 + 1, 1) - datetime.date(nam, thang, 1)).days
        print("Tháng nhập vào có", so_ngay_trong_thang, "ngày.")
    except ValueError:
        print("Ngày tháng năm không hợp lệ.")

xuly_ngay_thang()
