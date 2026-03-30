so = int(input("Nhập vào một số nguyên dương: "))

if so % 2 == 0 and so % 3 == 0:
    print(f"{so} chia hết cho cả 2 và 3.")
elif so % 2 == 0:
    print(f"{so} chỉ chia hết cho 2.")
elif so % 3 == 0:
    print(f"{so} chỉ chia hết cho 3.")
else:
    print(f"{so} không chia hết cho 2 cũng không chia hết cho 3.")