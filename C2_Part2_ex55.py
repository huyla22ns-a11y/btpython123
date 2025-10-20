import zipfile
import os

def compress_file(filename, zipname):
    with zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(filename, os.path.basename(filename))
    print(f"Đã nén {filename} thành {zipname}")

def decompress_file(zipname, extract_to="."):
    with zipfile.ZipFile(zipname, 'r') as zf:
        zf.extractall(extract_to)
    print(f"Đã giải nén {zipname} vào thư mục {extract_to}")

# Chương trình chính
print("1. Nén file")
print("2. Giải nén file")
choice = input("Chọn (1/2): ")

if choice == "1":
    fname = input("Nhập tên file cần nén: ")
    zname = input("Nhập tên file zip muốn tạo: ")
    compress_file(fname, zname)
elif choice == "2":
    zname = input("Nhập tên file zip cần giải nén: ")
    folder = input("Nhập thư mục đích (Enter để mặc định): ")
    if not folder.strip():
        folder = "."
    decompress_file(zname, folder)
else:
    print("Lựa chọn không hợp lệ.")