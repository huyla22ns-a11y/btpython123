num = int(input("Nhập vào một số: "))
level = int(input("Nhập bậc N: "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** level
    temp //= 10

if num == total:
    print(f"{num} là số Amstrong bậc {level}")
else:
    print(f"{num} không phải là số Amstrong bậc {level}")