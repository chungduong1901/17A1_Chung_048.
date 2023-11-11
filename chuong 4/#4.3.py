#4.3
m =int(input(" nhập số m bất kì: "))
n= int(input("nhập số n bất kì ( m nhỏ hơn n):"))
for i in range(1,n+1):
 if i%m==0:
  print(i,"là số chia hết cho m ")
 else :
  print(i,"là số không chia hết cho m ")