#8.12
def is_prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
n=int(input("nhập số tự nhiên "));
if is_prime(n):
    print(f"{n} là số nguyên tố ")
else:
    print(f"{n} không phải là số nguyên tố ")
