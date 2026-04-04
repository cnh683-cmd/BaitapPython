# Danh sách đầu vào như ví dụ của đề bài
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

gia_tri_dau_vao = int(input("Nhập vào độ dài tối thiểu: "))

dem = 0

for chuoi in _list:

    if len(chuoi) >= gia_tri_dau_vao and chuoi[0] == chuoi[-1]:
        dem += 1 
        print(f"-> Tìm thấy chuỗi thỏa mãn: '{chuoi}'")

print(f"\nKết quả đếm được: {dem} chuỗi")