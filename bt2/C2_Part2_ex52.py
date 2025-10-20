def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Chương trình chính
print("Các số hoàn hảo từ 1 đến 10000 là:")
for num in range(1, 10001):
    if is_perfect(num):
        print(num)