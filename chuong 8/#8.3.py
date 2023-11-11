#8.2
a=int(input("nhập a"));
b=int(input("nhập b"));
print("giải phương trình bậc nhât ax+b=0")
if(a==0 and b!=0):
    print(" phương trình vô nghiệm")
elif(a==0 and b==0):
    print("phương trình vô số nghiệm")
else:
    x=(-b)/a
    print("phương trinh có nghiệm x",x)