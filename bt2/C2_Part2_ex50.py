import random

def generate_password():
    length = random.randint(7, 10)  # độ dài 7–10 ký tự
    password = "".join(chr(random.randint(33, 126)) for _ in range(length))
    return password

# Chương trình chính
print("Mật khẩu ngẫu nhiên là:", generate_password())