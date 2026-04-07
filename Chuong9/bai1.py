class HocVien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    def show_info(self):
        thong_tin = (f"Họ tên: {self.ho_ten} | Ngày sinh: {self.ngay_sinh} | "
                     f"Email: {self.email} | SĐT: {self.dien_thoai} | "
                     f"Địa chỉ: {self.dia_chi} | Lớp: {self.lop}")
        return thong_tin

    def change_info(self, dia_chi='Hà Nội', lop='IT12.9'):
        self.dia_chi = dia_chi
        self.lop = lop


hv1 = HocVien("Nguyễn Hoàng Anh", "17/01/2005", "20230828@eaut.edu.vn", "0865997683", "Hà Đông", "IT12.2")

print("--- THÔNG TIN BAN ĐẦU ---")
print(hv1.show_info())

print("\n--- SAU KHI GỌI change_info (Không truyền tham số) ---")
hv1.change_info()
print(hv1.show_info())

print("\n--- SAU KHI GỌI change_info (Có truyền tham số mới) ---")
hv1.change_info(dia_chi="Thanh Hóa", lop="IT3.6")
print(hv1.show_info())