noi_dung = 'Thuc \nhanh \nvoi \nfile\nIO\n'
with open('demo_file1.txt', 'w', encoding='utf-8') as f:
    f.write(noi_dung)

print("a) In trên một dòng:")
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    mot_dong = " ".join(line.strip() for line in lines if line.strip())
    print(mot_dong)

print("\nb) In theo từng dòng:")
with open('demo_file1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())