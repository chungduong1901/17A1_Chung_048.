#10.6
import cmath 

def giai_pt_bac_2(a, b, c):
    S = b**2 - 4*a*c
    if S > 0:
        x1 = (-b + S**0.5) / (2*a)
        x2 = (-b - S**0.5) / (2*a)
        return x1, x2
    elif S == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + cmath.sqrt(S)) / (2*a)
        x2 = (-b - cmath.sqrt(S)) / (2*a)
        return x1, x2
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
nghiem = giai_pt_bac_2(a, b, c)
print("Nghiệm của phương trình là:", nghiem)
