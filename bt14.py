import math

# Nhập 2 số nguyên
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính toán
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra b khác 0 để tránh chia cho 0
if b != 0:
    thuong = a / b
    phan_du = a % b
else:
    thuong = "Không xác định (b = 0)"
    phan_du = "Không xác định (b = 0)"

# log10(a) — cần a > 0 mới hợp lệ
if a > 0:
    log10_a = math.log10(a)
else:
    log10_a = "Không xác định (a ≤ 0)"

# a^b
luy_thua = a ** b

# Xuất kết quả
print("Tổng a + b =", tong)
print("Hiệu a - b =", hieu)
print("Tích a * b =", tich)
print("Thương a / b =", thuong)
print("Phần dư a % b =", phan_du)
print("log10(a) =", log10_a)
print("a^b =", luy_thua)
