numlist = []

while True:
    inp = input("Nhập một số (gõ 'done' để kết thúc): ")
    if inp.lower() == "done":
        break
    try:
        value = float(inp)
        numlist.append(value)
    except ValueError:
        print("Vui lòng nhập số hợp lệ hoặc 'done' để kết thúc.")

if len(numlist) > 0:
    average = sum(numlist) / len(numlist)
    print("Giá trị trung bình:", average)
    print("Danh sách các số đã nhập:", numlist)
else:
    print("Không có số nào được nhập.")