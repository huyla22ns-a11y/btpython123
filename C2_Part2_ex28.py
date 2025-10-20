month = input("Nhập tên tháng (tiếng Anh): ").capitalize()

days_in_month = {
    "January": 31,
    "February": "28 hoặc 29",
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

if month in days_in_month:
    print(f"Tháng {month} có {days_in_month[month]} ngày.")
else:
    print("Tên tháng không hợp lệ! Vui lòng nhập đúng tên tháng bằng tiếng Anh.")