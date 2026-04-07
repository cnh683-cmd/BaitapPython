import ast

print(" ĐANG CHẠY CHƯƠNG TRÌNH MÃ HÓA...")

with open('mat_ma.txt', 'r', encoding='utf-8') as f:
    noi_dung_mat_ma = f.read()
    bang_ma = ast.literal_eval(noi_dung_mat_ma)

with open('van_ban_goc.txt', 'r', encoding='utf-8') as f:
    van_ban = f.read()

van_ban_ma_hoa = ""
for ky_tu in van_ban:
    if ky_tu in bang_ma:
        van_ban_ma_hoa += bang_ma[ky_tu]
    else:
        van_ban_ma_hoa += ky_tu

with open('ket_qua_ma_hoa.txt', 'w', encoding='utf-8') as f:
    f.write(van_ban_ma_hoa)

print(" Đã mã hóa xong! Hãy kiểm tra file 'ket_qua_ma_hoa.txt'.")