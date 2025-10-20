def print_first_5_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print(squares[:5])  # In 5 phần tử đầu tiên

# Ví dụ
print_first_5_squares()