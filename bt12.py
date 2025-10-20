# Nhập chi phí bữa ăn
gia_bua_an = float(input("Nhập chi phí bữa ăn (VNĐ): "))

# Tính tiền boa (18%) và tiền thuế (5%)
tien_boa = gia_bua_an * 0.18
tien_thue = gia_bua_an * 0.05

# Tính tổng tiền
tong_tien = gia_bua_an + tien_boa + tien_thue

# Hiển thị kết quả, định dạng 2 chữ số thập phân
print("Tiền bữa ăn: {:.2f}".format(gia_bua_an))
print("Tiền boa (18%): {:.2f}".format(tien_boa))
print("Tiền thuế (5%): {:.2f}".format(tien_thue))
print("Tổng cộng phải trả: {:.2f}".format(tong_tien))
