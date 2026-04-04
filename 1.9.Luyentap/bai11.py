_list = ["Tôi", "tên", "Nguyễn", "Hoàng", "Anh", "đẳng", "cấp"]

n = int(input("Nhập vào số nguyên n: "))

ket_qua = []

for tu in _list:
    if len(tu) > n:
        ket_qua.append(tu)

print(f"Danh sách ban đầu: {_list}")
print(f"Các từ có độ dài lớn hơn {n} là: {ket_qua}")