#8.4
import math
a=float(input("nhập cạnh a :"));
b=float(input("nhập cạnh b :"));
c=float(input("nhập cạnh c :"));
p=(a+b+c)/2
dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích tam giác ",p)