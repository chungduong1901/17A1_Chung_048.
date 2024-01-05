def kiem_tra_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print(kiem_tra_so_hoan_hao(28))  
print(kiem_tra_so_hoan_hao(12))  
