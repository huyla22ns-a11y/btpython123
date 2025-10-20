chuoi = input("Nhập vào các giá trị (cách nhau bởi dấu phẩy): ")

# Tách chuỗi thành list
kieu_ds = chuoi.split(",")

# Chuyển list thành tuple
kieu_tuples = tuple(kieu_ds)

# In kết quả
print(kieu_ds)
print(kieu_tuples)