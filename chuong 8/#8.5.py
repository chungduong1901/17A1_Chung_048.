#8.5
x=int(input("nhập năm :"));
if ((x%4==0 and x%100!=0)or(x%400==0)):
    print("đây là năm nhuận")
else:
    print("đây không phải năm nhuận")