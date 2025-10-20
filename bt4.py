# Nhập vào một chuỗi
chuoi = input("Nhập vào một chuỗi: ")

# Nhập từ cần thay thế
tu_cu = input("Nhập từ cần thay thế: ")

# Nhập từ thay thế mới
tu_moi = input("Nhập từ thay thế mới: ")

# Thực hiện thay thế
chuoi_moi = chuoi.replace(tu_cu, tu_moi)

# Hiển thị kết quả
print("Chuỗi sau khi thay thế:", chuoi_moi)
