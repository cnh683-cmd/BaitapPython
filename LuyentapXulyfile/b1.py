with open('data_b1.txt', 'w', encoding='utf-8') as f:
    f.write("Dòng 1: Xin chào\n")
    f.write("Dòng 2: Tôi tên Nguyễn Hoàng Anh\n")
    f.write("Dòng 3: Lớp DCCNTT.14.2\n")
    f.write("Dòng 4: Công nghệ Đông Á\n")
    f.write("Dòng 5: Đẳng cấp!")


try:
    n = int(input("Nhập số dòng n cần đọc: "))
    
    print(f"\n--- Đọc {n} dòng đầu tiên ---")
    with open('data_b1.txt', 'r', encoding='utf-8') as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line, end='')
    print("\n------------------------------")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")