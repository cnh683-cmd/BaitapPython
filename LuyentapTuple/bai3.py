_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

temp_list = []

for item in _tuple:
    if temp_list.count(item) == 0:
        temp_list.append(item)
        
_new_tuple = tuple(temp_list)

print(f"Tuple gốc: {_tuple}")
print(f"Tuple mới: {_new_tuple}")