st = input("Nhập vào một chuỗi: ")
st_search = input("Nhập vào chuỗi cần tìm: ")

if st_search in st:
    print("Đã tìm thấy chuỗi cần tìm, tại vị trí:", st.find(st_search))
else:
    print("Không tìm thấy")