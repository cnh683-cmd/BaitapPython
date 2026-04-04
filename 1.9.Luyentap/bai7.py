_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

print(f"List ban đầu: {_list}\n")

_new_1 = []
for item in _list:
    if _list.count(item) == 1:
        _new_1.append(item)
print(f"Kết quả Yêu cầu 1: {_new_1}")

_new_2 = []
for item in _list:
    if item not in _new_2:
        _new_2.append(item)
print(f"Kết quả Yêu cầu 2: {_new_2}")