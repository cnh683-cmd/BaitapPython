_a = int(input("Nhập cạnh _a: "))
_b = int(input("Nhập cạnh _b: "))
_c = int(input("Nhập cạnh _c: "))

if (_a + _b > _c) and (_a + _c > _b) and (_b + _c > _a):
    print("Độ dài ba canh tam giác")
else:
    print("Đây không phải độ dài ba canh tam giác")