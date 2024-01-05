#11.5
# Tạo list
numbers = []

# Nhập số phần tử trong list
n = int(input("Nhập số phần tử trong list: "))

# Cho phép người dùng lần lượt nhập các phần tử cho list
for i in range(n):
    num = int(input("Nhập phần tử thứ {}:".format(i+1)))
    numbers.append(num)

# Tìm và in ra tất cả các số nguyên tố có trong list
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print("Các số nguyên tố trong list:", prime_numbers)

# Tính trung bình cộng của các phần tử âm/ phần từ dương trong list
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

if len(positive_numbers) > 0:
    average_positive = sum(positive_numbers) / len(positive_numbers)
    print("Trung bình cộng của các phần tử dương trong list:", average_positive)
else:
    print("Không có phần tử dương trong list")

if len(negative_numbers) > 0:
    average_negative = sum(negative_numbers) / len(negative_numbers)
    print("Trung bình cộng của các phần tử âm trong list:", average_negative)
else:
    print("Không có phần tử âm trong list")

# Tìm giá trị lớn nhất/ nhỏ nhất trong list
max_value = max(numbers)
min_value = min(numbers)
print("Giá trị lớn nhất trong list:", max_value)
print("Giá trị nhỏ nhất trong list:", min_value)

# Sắp xếp list theo giá trị tăng dần
sorted_numbers = sorted(numbers)
print("List sau khi được sắp xếp:", sorted_numbers)
