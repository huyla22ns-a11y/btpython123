chuoi = input("Nhập vào một câu: ")
d = {"chu_hoa": 0, "chu_thuong": 0}

for ch in chuoi:
    if ch.isupper():      # Nếu là chữ hoa
        d["chu_hoa"] += 1
    elif ch.islower():    # Nếu là chữ thường
        d["chu_thuong"] += 1
    else:
        pass

print("Số chữ hoa là:", d["chu_hoa"])
print("Số chữ thường là:", d["chu_thuong"])