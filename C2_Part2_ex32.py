
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":  # Nếu là giải mã thì dịch ngược lại
        shift = -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Menu chọn
choice = input("Bạn muốn (E)ncrypt hay (D)ecrypt? ").lower()
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

if choice == 'e':
    encrypted = caesar_cipher(message, shift, "encrypt")
    print("Tin nhắn đã được mã hóa:", encrypted)
elif choice == 'd':
    decrypted = caesar_cipher(message, shift, "decrypt")
    print("Tin nhắn đã được giải mã:", decrypted)
else:
    print("Lựa chọn không hợp lệ!")