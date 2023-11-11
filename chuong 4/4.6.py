#Giải hệ phương trình:

         +---------------------+
         |      bắt đầu        | 
         +---------------------+ 
                  |
                  v
         +-----------------+
         | Nhập a, b, c     |
         +-----------------+
                  |
                  v
         +-----------------+
         | Δ = b^2 - 4ac   |
         +-----------------+
                  |
                  v
        Δ >= 0 ? ---------> Không ---------> Hiển thị "Vô nghiệm"
                  |                           |
                  v                           v
         +-----------------+         +-----------------+
         | x1 = (-b + √Δ)/2a |         | x2 = (-b - √Δ)/2a |
         +-----------------+         +-----------------+
                  |                           |
                  v                           v
         +-----------------+         +-----------------+
         | Hiển thị x1     |         | Hiển thị x2     |
         +-----------------+         +-----------------+
 -Giải thích:

Người dùng cần nhập các giá trị a, b, c của phương trình.
Tính delta (Δ) bằng công thức Δ = b^2 - 4ac.
Kiểm tra xem delta (Δ) có lớn hơn hoặc bằng 0 không. Nếu không, hiển thị "Vô nghiệm".
Nếu Δ lớn hơn hoặc bằng 0, tính và hiển thị hai nghiệm x1 và x2 sử dụng công thức.        

-#ính số ngày của một tháng một năm nào đó
         +---------------------+
         |      bắt đầu        | 
         +---------------------+   
                    |         
                    v
         +-----------------+
         | Nhập tháng, năm |
         +-----------------+
                  |
                  v
         +-----------------+
         | Tháng có 31 ngày?|------------------
         +-----------------+
                  |                           |
                  v                           v
         +-----------------+         +-----------------+
         | Hiển thị "31"   |         | Tháng 2?        |------
         +-----------------+         +-----------------+
                                            |                |
                                            v                |
         +-----------------+        +-----------------+      |
         |  Hiển thị "28"  |  <---- | Năm nhuận?      |      |
         +-----------------+        +-----------------+      |
                                            |                |
                                            v                v
                                    +-----------------+ +-----------------+
                                    | Hiển thị "29"   | | Hiển thị "30"   |
                                    +-----------------+ +-----------------+
.giải mã
Người dùng cần nhập tháng và năm.
Kiểm tra xem tháng có 31 ngày không. Nếu có, hiển thị 31.
Nếu không, kiểm tra xem tháng đó có phải tháng 2 không. 
Nếu là tháng 2, kiểm tra xem năm đó có phải là năm nhuận không.
Nếu là năm nhuận, hiển thị 29 ngày, ngược lại hiển thị 28 ngày.
Nếu không phải tháng 2, hiển thị 30 ngày.

#tìm ước số chung lớn nhất
         +---------------------+
         | Nhập a, b           |
         +---------------------+
                  |
                  v
         +---------------------+
         | a = max(a, b)      |
         +---------------------+
                  |
                  v
         +---------------------+
         | b = min(a, b)      |
         +---------------------+
                  |
                  v
         +---------------------+
         | WHILE a % b ≠ 0    |
         |    +---------------+
         |    | a = a % b      |
         |    | b = min(a, b)  |
         |    +---------------+
         +---------------------+
                  |
                  v
         +---------------------+
         | Hiển thị "USCLN là b"|
         +---------------------+
Giải mã:
1 Nhập a, b: Người dùng nhập hai số a và b.

2 Gán giá trị: Gán giá trị lớn hơn cho a và giá trị nhỏ hơn cho b.

3 Lặp cho đến khi a chia hết cho b:

 -a = a % b: Lấy phần dư khi a chia cho b và gán lại cho a.
 -Gán giá trị nhỏ hơn cho b: Gán giá trị nhỏ hơn giữa a và b cho b.
4 Hiển thị kết quả: Hiển thị giá trị cuối cùng của b, vì đó là ước số chung lớn nhất của a và b
Thuật toán sẽ tiếp tục lặp cho đến khi a chia hết cho b, và kết quả cuối cùng là ước số chung lớn nhất của a và b.