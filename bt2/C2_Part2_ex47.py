def print_squares_except_first_5():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print(squares[5:])  # Bỏ qua 5 phần tử đầu tiên

# Ví dụ
print_squares_except_first_5()