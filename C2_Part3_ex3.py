import os

# Lấy đường dẫn của file .py hiện tại (vd: bt3)
current_dir = os.path.dirname(__file__)

def ensure_file_exists(filename):
    """Kiểm tra nếu file chưa có thì tạo file mới trong cùng thư mục."""
    file_path = os.path.join(current_dir, filename)

    if not os.path.exists(file_path):
        print(f"⚠️ File '{filename}' chưa tồn tại. Đang tạo mới...")
        default_text = f"Đây là file {filename}. File này được tạo tự động để minh họa bài tập Python.\nChào mừng bạn đến với Python!"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(default_text)
        print(f"✅ File '{filename}' đã được tạo thành công tại: {file_path}\n")
    return file_path


def count_words(filename):
    """Đếm số từ trong file, tạo file nếu chưa có."""
    file_path = ensure_file_exists(filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"❌ Không thể mở file '{filename}'.")
        return

    words = contents.split()
    num_words = len(words)
    print(f"📄 File '{filename}' có {num_words} từ.\n")


# Danh sách file cần tạo và đếm
filenames = ['alice.txt', 'bob.txt']

for filename in filenames:
    count_words(filename)
