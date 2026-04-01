n = int(input("Nhập vào số nguyên n: "))

tong = 0
i = 1

while i < n:
    if i % 2 == 0:
        tong += i 
    i += 1 

print(f"Tổng của các số chẵn nhỏ hơn {n} là: {tong}")