import ast

print(" ĐANG CHẠY CHƯƠNG TRÌNH GIẢI MÃ...")

with open('mat_ma.txt', 'r', encoding='utf-8') as f:
    noi_dung_mat_ma = f.read()
    bang_ma = ast.literal_eval(noi_dung_mat_ma)
    
bang_giai_ma = {value: key for key, value in bang_ma.items()}

with open('ket_qua_ma_hoa.txt', 'r', encoding='utf-8') as f:
    van_ban_ma_hoa = f.read()

van_ban_giai_ma = ""
for ky_tu in van_ban_ma_hoa:
    if ky_tu in bang_giai_ma:
        van_ban_giai_ma += bang_giai_ma[ky_tu]
    else:
        van_ban_giai_ma += ky_tu

with open('ket_qua_giai_ma.txt', 'w', encoding='utf-8') as f:
    f.write(van_ban_giai_ma)

print(" Đã giải mã xong! Hãy kiểm tra file 'ket_qua_giai_ma.txt'.")