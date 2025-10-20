ds_tu = []
print("Nhập các từ (Enter để kết thúc):")

while True:
    tu = input()
    if tu == "":   # nếu dòng trống thì dừng
        break
    if tu not in ds_tu:   # chỉ thêm nếu chưa có trong danh sách
        ds_tu.append(tu)

print("\nKết quả sau khi loại bỏ trùng lặp:")
for t in ds_tu:
    print(t)
