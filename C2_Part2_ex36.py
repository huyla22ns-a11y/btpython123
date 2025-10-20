ds = []

while True:
    n = int(input("Nhập số nguyên (0 để dừng): "))
    if n == 0:
        break
    ds.append(n)

# Sắp xếp
ds.sort()

print("Các số đã nhập theo thứ tự tăng dần:")
for so in ds:
    print(so)