number = int(input("Nhập vào một số nguyên dương: "))

if number <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    if number % 2 == 0:
        print("Đây là số chẵn")
    else:
        print("Đây là số lẻ")