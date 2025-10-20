ftext = open("romeo.txt", "r", encoding="utf-8")

tu_dien_cac_tu = {}
for dong in ftext:
    danh_sach_tu = dong.split()
    for tu in danh_sach_tu:
        tu_dien_cac_tu[tu] = tu_dien_cac_tu.get(tu, 0) + 1

# Sắp xếp từ điển theo số lần xuất hiện (val) giảm dần
danh_sach = sorted(tu_dien_cac_tu.items(), key=lambda x: x[1], reverse=True)

# In ra 10 từ phổ biến nhất
for tu, solan in danh_sach[:10]:
    print(tu, solan)