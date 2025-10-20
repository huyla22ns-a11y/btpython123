st = input("Nhập vào một câu: ")

Sum_upper_Char = 0
Sum_lower_Char = 0

for c in st:
    if c.isupper():
        Sum_upper_Char += 1
    elif c.islower():
        Sum_lower_Char += 1
    else:
        pass

print("Chữ hoa:", Sum_upper_Char)
print("Chữ thường:", Sum_lower_Char)