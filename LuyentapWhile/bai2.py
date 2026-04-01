n = int(input("Nhập vào số nguyên dương n: "))

if n < 0:
    print("Không thể tính giai thừa cho số âm!")
else:
    giai_thua = 1
    i = 1
    
    while i <= n:
        giai_thua *= i
        i += 1
        
    print(f"Kết quả {n}! = {giai_thua}")