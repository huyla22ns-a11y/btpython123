j = []

for i in range(2000, 3201):  # từ 2000 đến 3200 (cả 2 đầu)
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))

print(",".join(j))