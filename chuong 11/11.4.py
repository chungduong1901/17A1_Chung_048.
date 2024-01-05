
numbers = []
while True:
    num = input("Nhập số (nhập 'dừng' nếu bạn đã nhập xong): ")
    if num == 'dừng':
        break
    else:
        numbers.append(int(num))
print("List các số:", numbers)
x = int(input("Nhập số x: "))
total = sum(numbers)
print("Tổng các số trong list:", total)
if x in numbers:
    print(x, "xuất hiện trong list")
    print(x, "xuất hiện", numbers.count(x), "lần trong list")
    print("Các số lớn hơn", x, "trong list:", [num for num in numbers if num > x])
else:
    print(x, "không xuất hiện trong list")
    print(x, "nhỏ hơn các số:", [num for num in numbers if num > x])
