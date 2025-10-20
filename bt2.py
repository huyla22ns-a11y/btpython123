# Chuỗi email ban đầu (có thể chứa ký tự lạ ở đầu)
email = "minhnhutvh@gmail.com"

# Loại bỏ ký tự đặc biệt ở đầu (nếu có)
email = email.strip()  # bỏ khoảng trắng đầu/cuối
if '@' in email:
    # Tách phần sau dấu @
    host = email.split('@')[1]
    print("Tên host là:", host)
else:
    print("Địa chỉ email không hợp lệ.")
