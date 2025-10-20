# Nhập nhiệt độ không khí và tốc độ gió
Ta = float(input("Nhập nhiệt độ không khí (°C): "))
V = float(input("Nhập tốc độ gió (km/h): "))

# Tính chỉ số gió lạnh
WCI = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)

# Làm tròn đến số nguyên gần nhất
WCI_rounded = round(WCI)

# Hiển thị kết quả
print("Chỉ số gió lạnh là:", WCI_rounded)
