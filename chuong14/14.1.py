# 14.1
def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài các cạnh phải là số dương và khác 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Độ dài các cạnh không thỏa mãn là một tam giác.")
    print("Đây là một tam giác hợp lệ.")
try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    kiem_tra_tam_giac(a, b, c)

except ValueError as ve:
    print(f"Lỗi: {ve}")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
