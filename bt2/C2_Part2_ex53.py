def all_subsets(lst):
    subsets = [[]]
    for num in lst:
        new_subsets = [s + [num] for s in subsets]
        subsets.extend(new_subsets)
    return subsets

# Ví dụ
print("Tất cả danh sách con của [1, 2, 3]:")
print(all_subsets([1, 2, 3]))