import math

# Gia tốc trọng trường
g = 9.8  # m/s^2
v_i = 0  # tốc độ ban đầu

# Nhập chiều cao
d = float(input("Nhập chiều cao thả vật (m): "))

# Tính tốc độ cuối cùng
v_f = math.sqrt(v_i**2 + 2 * g * d)

# Hiển thị kết quả
print("Tốc độ của vật khi chạm đất là: {:.2f} m/s".format(v_f))
