lines = []
print("Nhập nhiều dòng (nhấn Enter trống để kết thúc):")

while True:
    s = input()
    if s:   # nếu dòng không rỗng thì thêm vào list
        lines.append(s.upper())
    else:   # nếu dòng rỗng thì dừng
        break

# In kết quả
print("\nKết quả sau khi chuyển thành chữ in hoa:")
for sentence in lines:
    print(sentence)