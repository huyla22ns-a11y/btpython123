def print_last_5_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    print(squares[-5:])  # Lấy 5 phần tử cuối cùng

# Ví dụ
print_last_5_squares()