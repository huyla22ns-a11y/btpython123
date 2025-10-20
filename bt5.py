# Nhập vào một chuỗi
chuoi = input("Nhập vào một chuỗi: ")

# Lấy 5 ký tự đầu và 5 ký tự cuối
dau = chuoi[:5]
cuoi = chuoi[-5:]

# Xuất ra 4 chuỗi:
#  - Chuỗi gốc
#  - 5 ký tự đầu
#  - 5 ký tự cuối
#  - Độ dài chuỗi (nếu bạn cần, có thể đổi sang chuỗi khác)

# 4 chuỗi trên một dòng, cách nhau bởi khoảng trắng
print(chuoi, dau, cuoi, sep=' ')

# 4 chuỗi trên 4 dòng
print(chuoi)
print(dau)
print(cuoi)
