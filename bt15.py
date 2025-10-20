# Nhiệt dung riêng của nước
C = 4.186  # J/g°C

# Hằng số đổi đơn vị
J_to_kWh = 2.777e-7
cost_per_kWh = 8.9  # cent/kWh

# Nhập dữ liệu từ người dùng
M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập độ thay đổi nhiệt độ ΔT (°C): "))

# Tính năng lượng cần thiết
Q = M * C * delta_T  # đơn vị: Joules

# Đổi sang kWh
Q_kWh = Q * J_to_kWh

# Tính chi phí (cent)
cost = Q_kWh * cost_per_kWh

# Hiển thị kết quả
print("\n--- KẾT QUẢ ---")
print("Năng lượng cần thiết: {:.2f} Joules".format(Q))
print("Năng lượng cần thiết: {:.6f} kWh".format(Q_kWh))
print("Chi phí ước tính: {:.4f} cent".format(cost))
