
list = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
heights_meter = [height * 0.0254 for height in list]
print("3 chiều cao cuối cùng:", heights_meter[-3:])
average_height = sum(heights_meter) / len(heights_meter)
max_height = max(heights_meter)
min_height = min(heights_meter)
print("Chiều cao trung bình:", average_height)
print("Chiều cao lớn nhất:", max_height)
print("Chiều cao nhỏ nhất:", min_height)

sorted_heights = sorted(heights_meter)
print("List sau khi được sắp xếp tăng dần:", sorted_heights)

sorted_heights_reverse = sorted(heights_meter, reverse=True)
print("List sau khi được sắp xếp giảm dần:", sorted_heights_reverse) 
