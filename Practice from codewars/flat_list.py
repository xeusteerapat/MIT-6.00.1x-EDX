l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

flat_list = []
for sub_list in l:
    for item in sub_list:
        flat_list.append(item)

print(flat_list)
