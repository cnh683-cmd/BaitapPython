a = int(input("Nhập số nguyên thứ nhất (a): "))
b = int(input("Nhập số nguyên thứ hai (b): "))
c = int(input("Nhập số nguyên thứ ba (c): "))

tong_3so = a + b + c
tich_3so = a * b * c
print(f"\na) Tổng 3 số: {tong_3so}")
print(f"   Tích 3 số: {tich_3so}")

hieu_ab = a - b
print(f"b) Hiệu của a và b (a - b) là: {hieu_ab}")


if b != 0:
    chia_nguyen = a // b
    chia_du = a % b
    chia_chinh_xac = a / b
    
    print("c) Phép chia a cho b:")
    print(f"   - Chia lấy phần nguyên: {chia_nguyen}")
    print(f"   - Chia lấy phần dư: {chia_du}")
    print(f"   - Kết quả chính xác: {chia_chinh_xac}")
else:
    print("c) Không thể thực hiện phép chia vì b = 0.")