#8.8
lp=int(input("nhập loại phòng từ 1-8:"));
sd=int(input(" nhập số đêm "));
if (lp ==1 ):
    print(" tên phòng Standard")
    if (sd >=2 and sd <= 3):
        tt=(1260000-(1260000*0.25))*sd
        print(" thành tiền =",tt)
    elif (sd >= 4):
        tt=(1260000-(1260000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=sd*1260000
        print(" thành tiên =",tt)
if (lp ==2):
    print(" tên phòng superior Garden View")
    if (sd>=2 and sd <=3):
        tt=(1550000-(1550000*0.25))*sd
        print(" thành tiên =",tt)
    elif(sd>=4):
        tt=(1550000-(1550000*0.3))*sd
        print(" thành tiên =",tt)
    else:
        tt=1550000*sd
        print(" thành tiền =",tt)
if(lp ==3):
    print("tên phòng Super Ocean View")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp ==4):
    print("tên phòng Garden View Bungalow")
    if (sd >=2 and sd <=3):
        tt=(1830000-(1830000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd >=4):
        tt=(1830000-(1830000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=1830000*sd
        print(" thành tiền =",tt)
if(lp==5):
    print("tên phòng Pool View Bungalow")
    if (sd>=2 and sd<=3):
        tt=(2120000-(2120000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(2120000-(2120000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=2120000*sd
        print(" thành tiền =",tt)
if(lp==6):
     print("tên phòng Family Room ")
     if (sd>=2 and sd<=3):
            tt=(2120000-(2120000*0.25))*sd
            print(" thành tiền =",tt)
     elif(sd>=4):
            tt=(2120000-(2120000*0.3))*sd
            print(" thành tiền =",tt)
     else:
            tt=2120000*sd
            print(" thành tiền =",tt)
if (lp==7):
    print("tên phòng Beach Front Bungalow")
    if(sd>=2 and sd<=3):
        tt=(2540000-(2540000*0.25))*sd
        print(" thanh tiền =",tt)
    elif(sd>=4):
        tt=(2540000-(2540000*0.3))*sd
        print("  thành tiền =",tt)
    else:
        tt=2540000*sd
        print(" thành tiền =",tt)
if(lp==8):
    print("tên phòng VIP sea View")
    if (sd>=2 and sd<=3):
        tt=(4800000-(4800000*0.25))*sd
        print(" thành tiền =",tt)
    elif(sd>=4):
        tt=(4800000-(4800000*0.3))*sd
        print(" thành tiền =",tt)
    else:
        tt=4800000*sd
        print(" thành tiền =",tt)     