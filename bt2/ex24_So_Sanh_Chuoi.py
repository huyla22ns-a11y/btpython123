def printValue(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print("Chuỗi dài hơn:", s1)
    elif len2 > len1:
        print("Chuỗi dài hơn:", s2)
    else:
        print("Hai chuỗi có độ dài bằng nhau:")
        print(s1)
        print(s2)
