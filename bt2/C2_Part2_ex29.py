a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

# Kiểm tra có tạo thành tam giác hợp lệ không
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        print("Tam giác cân.")
    else:
        print("Tam giác thường.")
else:
    print("Ba cạnh này không tạo thành tam giác hợp lệ!")