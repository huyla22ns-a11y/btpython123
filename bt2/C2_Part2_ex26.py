letter = input("Nhập một chữ cái: ").lower()

if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"Chữ cái '{letter}' là nguyên âm.")
elif letter == 'y':
    print("Chữ cái 'y' có thể là nguyên âm hoặc phụ âm.")
else:
    print(f"Chữ cái '{letter}' là phụ âm.")