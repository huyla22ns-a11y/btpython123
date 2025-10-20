total = 0
count = 0

while True:
    inp = input("Nhập một số (gõ 'done' để kết thúc): ")
    if inp.lower() == "done":   # Cho phép nhập done hoặc DONE đều được
        break
    try:
        value = float(inp)
        total += value
        count += 1
    except ValueError:
        print("Vui lòng nhập số hợp lệ hoặc 'done' để kết thúc.")

if count > 0:
    average = total / count
    print("Giá trị trung bình là:", average)
else:
    print("Không có số nào được nhập.")