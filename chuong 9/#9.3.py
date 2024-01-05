#9.3
def tinh_BMI(can_nang, chieu_cao):
    BMI = can_nang / (chieu_cao * chieu_cao)
    return BMI

def danh_gia_BMI(BMI):
    if BMI < 18.5:
        return "Gầy"
    elif 18.5 <= BMI < 25:
        return "Bình thường"
    else:
        return "Thừa cân"

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

BMI = tinh_BMI(can_nang, chieu_cao)
print(f"Chỉ số BMI của bạn là: {BMI:.2f}")
print(f"Phân loại BMI của bạn là: {danh_gia_BMI(BMI)}")
