#6.9
lai_xuat_mot_nam = float(input('nhập lãi suất một năm:'))
so_tien_gui = int(input('nhập số tiền gửi:'))
so_thang_gui = int(input('nhập số tháng gửi:'))
so_tien_lai = (so_tien_gui*so_thang_gui)*(lai_xuat_mot_nam/100/12)
print('tiền lãi:',(so_tien_gui*so_thang_gui)*(lai_xuat_mot_nam/100/12))
print('tiền vốn + lãi:',so_tien_gui+so_tien_lai)