#8.16
def find_gcd(a,b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
gdc = find_gcd(a,b)
print(f"UCLN của {a} và {b} là: {find_gcd}")