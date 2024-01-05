def nam_am_lich(nam_duong_lich):
    can = nam_duong_lich % 10
    chi = nam_duong_lich % 12

    can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    nam_am = can_list[can] + " " + chi_list[chi]

    return nam_am

nam_duong_lich = 2017
nam_am = nam_am_lich(nam_duong_lich)
print(f"Năm {nam_duong_lich} lịch âm là năm {nam_am}")
