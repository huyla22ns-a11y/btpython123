def Tao_In_DS():
    ds = []
    for i in range(1, 21):
        ds.append(i**2)
    print("5 phần tử đầu + 5 phần tử cuối:")
    print(ds[:5] + ds[-5:])

# Thực thi hàm
Tao_In_DS()