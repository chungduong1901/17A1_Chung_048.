#8.19
def dao_nguoc_day_so_so_le(n):
    day_so = list(range(1,2*n, 2))
    day_so_dao_nguoc = day_so[::-1]
    return day_so_dao_nguoc 
so_luong = int(input("Nhập số lượng số trong dãy:"))
ket_qua = dao_nguoc_day_so_so_le(so_luong)
print("Dãy số đâỏ ngược:", ket_qua)
