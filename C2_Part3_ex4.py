import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

# -------------------------------
# 🗜️ Hàm nén thư mục
# -------------------------------
def compress_folder():
    """Chọn thư mục từ ổ đĩa và nén thành file .zip ngay tại đó."""
    folder_path = filedialog.askdirectory(
        title="Chọn thư mục để nén (từ ổ đĩa bất kỳ)"
    )
    if not folder_path:
        messagebox.showwarning("Thông báo", "Bạn chưa chọn thư mục nào.")
        return

    zip_name = folder_path.rstrip("\\/") + ".zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(folder_path))
                zipf.write(full_path, arcname=rel_path)

    messagebox.showinfo(
        "✅ Thành công",
        f"Đã nén thư mục:\n{folder_path}\n\nThành file:\n{zip_name}"
    )


# -------------------------------
# 📦 Hàm giải nén file zip
# -------------------------------
def decompress_zip():
    """Chọn file ZIP từ ổ đĩa và giải nén ra cùng vị trí."""
    zip_path = filedialog.askopenfilename(
        title="Chọn file ZIP để giải nén",
        filetypes=[("ZIP files", "*.zip")]
    )
    if not zip_path:
        messagebox.showwarning("Thông báo", "Bạn chưa chọn file ZIP nào.")
        return

    extract_dir = zip_path.rstrip(".zip") + "_extract"

    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(extract_dir)

    messagebox.showinfo(
        "✅ Thành công",
        f"Đã giải nén file:\n{zip_path}\n\nVào thư mục:\n{extract_dir}"
    )


# -------------------------------
# 🪟 Giao diện chính
# -------------------------------
root = tk.Tk()
root.title("🗜️ Công cụ Nén & Giải nén ZIP")
root.geometry("420x230")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Tiêu đề
label = tk.Label(
    root,
    text="Chọn chức năng bạn muốn thực hiện:",
    font=("Arial", 13, "bold"),
    bg="#f0f0f0"
)
label.pack(pady=20)

# Nút Nén
compress_btn = tk.Button(
    root,
    text="🗜️ Nén thư mục",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#4CAF50",
    fg="white",
    relief="ridge",
    command=compress_folder
)
compress_btn.pack(pady=10)

# Nút Giải nén
decompress_btn = tk.Button(
    root,
    text="📦 Giải nén file ZIP",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#2196F3",
    fg="white",
    relief="ridge",
    command=decompress_zip
)
decompress_btn.pack(pady=10)

# Nút Thoát
exit_btn = tk.Button(
    root,
    text="❌ Thoát",
    font=("Arial", 11),
    width=10,
    bg="#f44336",
    fg="white",
    command=root.destroy
)
exit_btn.pack(pady=10)

root.mainloop()
