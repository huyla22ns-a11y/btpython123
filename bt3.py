# Chuỗi ban đầu
chuoi = 'minhnhutvh@gmai.comSatJan509:14:16'

# Tách các phần bằng ký tự 
parts = chuoi.split('')

# Lấy phần email ở đầu
email = parts[0]

# Tách phần sau dấu @ để lấy tên host
if '@' in email:
    host = email.split('@')[1]
    print("Tên host là:", host)
else:
    print("Không tìm thấy địa chỉ email hợp lệ.")
