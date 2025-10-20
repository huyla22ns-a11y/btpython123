def format_words(words):
    if not words:   # Nếu danh sách rỗng
        return ""
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return f"{words[0]} and {words[1]}"
    return ", ".join(words[:-1]) + " and " + words[-1]

# Chương trình chính
lst = []
print("Nhập từ (Enter trống để kết thúc):")
while True:
    word = input("> ").strip()
    if word == "":
        break
    lst.append(word)

print("Kết quả định dạng:")
print(format_words(lst))