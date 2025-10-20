my_str = input("Nhập một chuỗi: ")

st2 = ""
for char in my_str:
    if char.isalnum() or char.isspace():   
        st2 += char

print("Chuỗi sau khi loại bỏ:", st2)