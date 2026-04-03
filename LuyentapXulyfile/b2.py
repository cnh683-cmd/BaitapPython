# Yêu cầu nhập văn bản
van_ban = input("Nhập đoạn văn bản bạn muốn lưu: ")
with open('bai2_output.txt', 'w', encoding='utf-8') as f:
    f.write(van_ban)
print("-> Đã lưu vào file 'bai2_output.txt'")
print("\n--- Nội dung vừa lưu trong file ---")
with open('bai2_output.txt', 'r', encoding='utf-8') as f:
    noidung_doc_duoc = f.read()
    print(noidung_doc_duoc)