def caesar_encrypt(text):
    result = ""
    shift = 3
    for char in text:
        if char.isalpha():
            # Giữ nguyên chữ hoa và chữ thường
            start = ord('A') if char.isupper() else ord('a')
            # Dịch chuyển trong phạm vi 26 chữ cái
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Nhập chuỗi từ người dùng
plain_text = input("Nhập tin nhắn cần mã hóa: ")
cipher_text = caesar_encrypt(plain_text)
print("Tin nhắn đã được mã hóa:", cipher_text)