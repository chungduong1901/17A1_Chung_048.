#8.17
def tim_ucln(a,b):
    while b:
        a,b = b,a%b
    return a
def tim_bcnn(a, b):
    return a* b// tim_ucln(a,b)
a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
print(f"BCLN của {a} và {b} là {tim_bcnn(a,b)}")