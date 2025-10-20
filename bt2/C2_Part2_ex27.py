sides = int(input("Nhập số cạnh của hình: "))

shapes = {
    3: "Tam giác",
    4: "Tứ giác",
    5: "Ngũ giác",
    6: "Lục giác",
    7: "Thất giác",
    8: "Bát giác",
    9: "Cửu giác",
    10: "Thập giác"
}

if sides in shapes:
    print(f"Hình có {sides} cạnh là: {shapes[sides]}")
else:
    print("Số cạnh không hợp lệ! Chỉ hỗ trợ từ 3 đến 10 cạnh.")