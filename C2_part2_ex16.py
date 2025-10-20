n = int(input("Nhập vào một số: "))
d = {}   # Khởi tạo từ điển rỗng

for i in range(1, n+1):
    d[i] = i * i   # Gán giá trị bình phương cho khóa i

print(d)