def is_good_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

# Chương trình chính
pw = input("Nhập mật khẩu: ")
if is_good_password(pw):
    print("Mật khẩu mạnh (tốt).")
else:
    print("Mật khẩu chưa đạt yêu cầu.")