#8.6
loaixe=int(input("nhập loại xe 4 chỗ hoặc 7 chỗ :"));
sokm=int(input("nhập số km :"));
tgtro=int(input("nhập thời gian chờ :"));
if (tgtro >=5):
    tientro=(tgtro-5)*800
    print("tiền chờ ",tientro)
else:
    print("05 phút đầu được miễn phí tiền trờ")
if(loaixe ==4):
    if(sokm<=20):
        tiendichuyen=12100*sokm
        tiencuoc=(tiendichuyen+tientro)
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(20*12100)+((sokm-20)*10000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
if(loaixe==7):
    if(sokm<=30):
        tiendichuyen=14100*sokm
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)
    else:
        tiendichuyen=(30*14100)+((sokm-30)*12000)
        tiencuoc=tiendichuyen+tientro
        print("tiền di chuyển ",tiendichuyen)
        print("tiên cước ",tiencuoc)