n = int(input("Nhập một số nguyên lớn hơn 0: "))

if n > 0:
    total = 0.0
    for i in range(1, n + 1):
        total += i / (i + 1)
    print("Tổng =", total)
else:
    print("Vui lòng nhập số nguyên dương lớn hơn 0")