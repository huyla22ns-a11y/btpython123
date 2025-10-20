def print_longer_string(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

# Ví dụ
print_longer_string("hello", "world!")
print_longer_string("abc", "xyz")