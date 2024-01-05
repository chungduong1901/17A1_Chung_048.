#9.5
def tinh_S(n, x):
    S = (x*x + x + 1) ** n + (x*x - x + 1) ** n
    return S

n = int(input("Nhập giá trị của n: "))
x = int(input("Nhập giá trị của x: "))

ket_qua = tinh_S(n, x)
print(f"Giá trị của S là: {ket_qua}")
