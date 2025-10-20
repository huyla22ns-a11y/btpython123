import os

# Lấy đường dẫn thư mục chứa file Python hiện tại
current_dir = os.path.dirname(__file__)

# Tạo đường dẫn đầy đủ cho alice.txt
filename = os.path.join(current_dir, 'alice.txt')

try:
    with open(filename, 'r', encoding='utf-8') as f_obj:
        contents = f_obj.read()
        print("✅ Nội dung file:")
        print(contents)
except FileNotFoundError:
    print(f"⚠️ File '{filename}' chưa tồn tại. Tạo mới file...")
    default_text = "Đây là nội dung mặc định được tạo tự động.\nChào mừng bạn đến với Python File Handling!"
    with open(filename, 'w', encoding='utf-8') as f_obj:
        f_obj.write(default_text)
    print(f"✅ File '{filename}' đã được tạo trong thư mục bt3!")
