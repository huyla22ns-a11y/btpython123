st = input("Nhập vào một chuỗi: ")

if st.isupper():
    print("Đây là chuỗi viết HOA")
elif st.islower():
    print("Đây là chuỗi viết thường")
else:
    print("Chuỗi này chứa cả ký tự HOA và ký tự thường")