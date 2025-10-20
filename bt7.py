import math

# Nhập 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Nhập 3 góc (radian)
A = float(input("Nhập góc A (radian): "))
B = float(input("Nhập góc B (radian): "))
C = float(input("Nhập góc C (radian): "))

# Tính diện tích theo công thức 1/2 * a * b * sin(C)
S = 0.5 * a * b * math.sin(C)
print("Diện tích tam giác là:", S)
