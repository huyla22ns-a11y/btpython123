# Bài 2: Xử lý ngoại lệ FileNotFoundError khi đếm số từ trong file text

filename = 'alice.txt'  # Tên file cần đọc

try:
    # Mở file và đọc nội dung
    with open(filename, 'r', encoding='utf-8') as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    # Nếu file không tồn tại, in thông báo lỗi
    msg = "⚠️ File '" + filename + "' không tồn tại."
    print(msg)

else:
    # Nếu file tồn tại, đếm số từ trong file
    words = contents.split()           # Tách nội dung thành danh sách các từ
    num_words = len(words)             # Đếm số lượng phần tử (tức là số từ)
    print(f"✅ File '{filename}' có {num_words} từ.")
