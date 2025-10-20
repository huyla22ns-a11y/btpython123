import math

# Nhập cạnh tam giác đều
a = float(input("Nhập cạnh tam giác đều: "))

# Tính theo định lý Heron
p = (3*a) / 2
S = math.sqrt(p * (p - a) * (p - a) * (p - a))
print("Diện tích tam giác đều là:", S)
