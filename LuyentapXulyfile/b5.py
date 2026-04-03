from collections import Counter

noi_dung = 'Dem so luong tu xuat hien abc abc abc 12 12 it it eaut'
with open('demo_file2.txt', 'w', encoding='utf-8') as f:
    f.write(noi_dung)

with open('demo_file2.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
    danh_sach_tu = text.split()
    
    ket_qua = dict(Counter(danh_sach_tu))
    
    print("Kết quả trả về:")
    print(ket_qua)