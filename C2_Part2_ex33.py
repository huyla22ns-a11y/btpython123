chuoi = input("Nhập một chuỗi: ")

# Đảo ngược chuỗi và so sánh
if chuoi == chuoi[::-1]:
    print(f'"{chuoi}" là Palindrome!')
else:
    print(f'"{chuoi}" không phải là Palindrome.')