#9.6
def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
print(kiem_tra_so_nguyen_to(7)) 
