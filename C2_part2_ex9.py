my_str = "Hello this Is an Example With cased letters"



# Tách từ trong chuỗi và lưu vào danh sách
ds_tu = my_str.split()

# Sắp xếp các phần tử trong danh sách
ds_tu.sort()

# Hiển thị danh sách sau khi sắp xếp
print("Các từ đã được tách và sắp xếp theo Alphabet:")
for tu in ds_tu:
    print(tu)