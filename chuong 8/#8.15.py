#8.15
total = 0
while True:
    try:
        num = int(input("Nhập số nguyên (nhập 0 để kết thúc):"))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ")
print("S=:", total)