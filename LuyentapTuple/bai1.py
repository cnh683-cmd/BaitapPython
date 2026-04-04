_tuple = ('a', 'b', 'd', 'e')

print(f"Tuple ban đầu: {_tuple}")

temp_list = list(_tuple)

temp_list.insert(2, 'c')

_new_tuple = tuple(temp_list)

print(f"Tuple mới sau khi chèn: {_new_tuple}")
