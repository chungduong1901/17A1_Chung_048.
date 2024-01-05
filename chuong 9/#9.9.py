#9.9
tinh_dien_tich_chu_vi_hinh_tron = lambda r: (3.14 * r**2, 2 * 3.14 * r)
tinh_dien_tich_chu_vi_hinh_chu_nhat = lambda a, b: (a * b, 2 * (a + b))
r = int(input("nhập r :"))
a = int(input("nhập a :"))
b = int(input("nhập b :"))
print("Diện tích và chu vi hình tròn:", tinh_dien_tich_chu_vi_hinh_tron(r))
print("Diện tích và chu vi hình chữ nhật:", tinh_dien_tich_chu_vi_hinh_chu_nhat(a, b))
