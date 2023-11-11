#8.18
def kiem_tra_so_hoan_hao(x):
    tong = 0
    for i in range(1,x):
        if x % i == 0:
            tong +=i
    return tong == x 
x = int(input("Nhập một số x:"))
if kiem_tra_so_hoan_hao(x):
    pritn(f"{x} là số hoàn hảo.")
else:
    print(f"{x} không phải là số hoàn hảo")