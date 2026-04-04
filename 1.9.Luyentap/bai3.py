_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_even = []
list_odd = []

for so in _list:
    if so % 2 == 0:
        list_even.append(so)
    else:
        list_odd.append(so)

print(f"List số chẵn (even): {list_even}")
print(f"List số lẻ (odd): {list_odd}")