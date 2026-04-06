bang_ma = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

bang_giai_ma = {value: key for key, value in bang_ma.items()}

def ma_hoa(van_ban):
    ket_qua = ""
    for ky_tu in van_ban:
        if ky_tu in bang_ma:
            ket_qua += bang_ma[ky_tu]
        else:
            ket_qua += ky_tu
    return ket_qua

def giai_ma(van_ban_ma_hoa):
    ket_qua = ""
    for ky_tu in van_ban_ma_hoa:
        if ky_tu in bang_giai_ma:
            ket_qua += bang_giai_ma[ky_tu]
        else:
            ket_qua += ky_tu
    return ket_qua

chuoi_goc = "abcd bad cab"
print(f"Chuỗi gốc: {chuoi_goc}")

chuoi_ma_hoa = ma_hoa(chuoi_goc)
print(f"Sau khi mã hóa: {chuoi_ma_hoa}")

chuoi_giai_ma = giai_ma(chuoi_ma_hoa)
print(f"Sau khi giải mã: {chuoi_giai_ma}")