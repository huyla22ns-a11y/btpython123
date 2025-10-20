
so_am = []
so_0 = []
so_duong = []

print("Nhập các số nguyên (Enter để kết thúc):")

while True:
    dong = input()
    if dong == "":   # nếu dòng trống thì dừng
        break
    n = int(dong)
    if n < 0:
        so_am.append(n)
    elif n == 0:
        so_0.append(n)
    else:
        so_duong.append(n)

# Ghép kết quả theo yêu cầu: âm -> 0 -> dương
ket_qua = so_am + so_0 + so_duong

print("\nKết quả:")
for x in ket_qua:
    print(x)