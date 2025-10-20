# Nhập: 1,2,3,4,5,6,7,8,9
day_so = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành list số nguyên
so_list = [int(x) for x in day_so.split(",")]

# Lọc số lẻ
so_le = [x for x in so_list if x % 2 != 0]

print("Các số lẻ là:", so_le)