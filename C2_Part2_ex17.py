chuoi = input("Nhập vào một câu: ")
d = {"chu_cai": 0, "chu_so": 0}

for ch in chuoi:
    if ch.isalpha():      # Nếu là chữ cái
        d["chu_cai"] += 1
    elif ch.isdigit():    # Nếu là chữ số
        d["chu_so"] += 1
    else:
        pass

print("Số chữ cái là:", d["chu_cai"])
print("Số chữ số là:", d["chu_so"])