year = int(input("Nhập một năm: "))

if year % 400 == 0:
    print(f"Năm {year} là năm nhuận.")
elif year % 100 == 0:
    print(f"Năm {year} không phải là năm nhuận.")
elif year % 4 == 0:
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")