#7.7
def doi_tien(so_tien):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to = []
    for menh_gia_i in menh_gia:
        so_to_i = so_tien // menh_gia_i
        so_to.append(so_to_i)
        so_tien %= menh_gia_i

    return so_to, so_tien
so_tien_muon_doi = int(input("Số tiền muốn đổi: "))
so_to, so_tien_con_lai = doi_tien(so_tien_muon_doi)
print("Số tờ 500,000:", so_to[0])
print("Số tờ 200,000:", so_to[1])
print("Số tờ 100,000:", so_to[2])
print("Số tờ 50,000:", so_to[3])
print("Tiền còn lại:", so_tien_con_lai)