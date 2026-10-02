"""
TUẦN 8 — DUNDER METHODS (__ten__)

"dunder" = double underscore. Đây là cách class của bạn tham gia vào
các cú pháp có sẵn của Python: print(), ==, <, +, len(), in, for.

Ở file 13 ta thấy len() hoạt động với mọi kiểu. Giờ bạn tự làm được.

Chạy: python 17_dunder_methods.py
"""

# ---------------------------------------------------------------
# 1. __str__ VÀ __repr__
# ---------------------------------------------------------------
print("1. __str__ VÀ __repr__")


class DiemKhongCo:
    def __init__(self, x, y):
        self.x, self.y = x, y


print(f"   không có __str__: {DiemKhongCo(1, 2)}")
print("   ← vô dụng khi debug")


class Diem:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Cho NGƯỜI đọc — print() dùng cái này."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Cho LẬP TRÌNH VIÊN — nên là code tạo lại được object."""
        return f"Diem({self.x}, {self.y})"


p = Diem(1, 2)
print(f"\n   print(p)  → {p}")
print(f"   repr(p)   → {p!r}")
print(f"   trong list → {[Diem(1, 2), Diem(3, 4)]}   ← list dùng __repr__")

print("""
   Quy tắc: nếu chỉ viết được một cái, viết __repr__ — vì print() sẽ
   dùng __repr__ khi không có __str__, và __repr__ giúp debug.""")


# ---------------------------------------------------------------
# 2. __eq__ — SO SÁNH BẰNG
# ---------------------------------------------------------------
print("2. __eq__")

a, b = DiemKhongCo(1, 2), DiemKhongCo(1, 2)
print(f"   không có __eq__: DiemKhongCo(1,2) == DiemKhongCo(1,2) → {a == b}")
print("   ← mặc định Python so sánh ĐỊA CHỈ, không so sánh nội dung")


class DiemSoSanh:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"DiemSoSanh({self.x}, {self.y})"

    def __eq__(self, khac):
        if not isinstance(khac, DiemSoSanh):
            return NotImplemented          # để Python thử cách khác
        return (self.x, self.y) == (khac.x, khac.y)

    def __hash__(self):
        """Có __eq__ thì NÊN có __hash__, nếu không object không vào set/dict."""
        return hash((self.x, self.y))


c, d = DiemSoSanh(1, 2), DiemSoSanh(1, 2)
print(f"\n   có __eq__: {c} == {d} → {c == d}")
print(f"   dùng được trong list: DiemSoSanh(1,2) in [...] → {DiemSoSanh(1, 2) in [c, d]}")
print(f"   dùng được trong set: {len({c, d})} phần tử  ← nhờ __hash__")

# Lưu ý: định nghĩa __eq__ mà quên __hash__ thì Python tự đặt __hash__ = None,
# object sẽ không dùng được làm khóa dict hay phần tử set.


# ---------------------------------------------------------------
# 3. __lt__ — SẮP XẾP ĐƯỢC
# ---------------------------------------------------------------
print("\n3. __lt__ VÀ sorted()")


class SinhVien:
    def __init__(self, ten, diem):
        self.ten, self.diem = ten, diem

    def __repr__(self):
        return f"{self.ten}({self.diem})"

    def __lt__(self, khac):
        """Chỉ cần __lt__ là sorted(), min(), max() đều hoạt động."""
        return self.diem < khac.diem


lop = [SinhVien("Minh", 8.5), SinhVien("Lan", 9.2), SinhVien("Hùng", 7.0)]
print(f"   sorted():  {sorted(lop)}")
print(f"   max():     {max(lop)}")
print(f"   min():     {min(lop)}")
print("   ← không cần key=lambda nữa")


# ---------------------------------------------------------------
# 4. __len__, __getitem__, __contains__, __iter__
# ---------------------------------------------------------------
print("\n4. LÀM CLASS HOẠT ĐỘNG NHƯ MỘT TẬP HỢP")


class LopHoc:
    def __init__(self, ten):
        self.ten = ten
        self._sv = []

    def them(self, sv):
        self._sv.append(sv)
        return self

    def __len__(self):
        return len(self._sv)

    def __getitem__(self, i):
        return self._sv[i]              # cho phép lop[0] và lop[1:3]

    def __contains__(self, sv):
        return sv in self._sv           # cho phép `in`

    def __iter__(self):
        return iter(self._sv)           # cho phép `for`

    def __repr__(self):
        return f"LopHoc({self.ten!r}, {len(self)} sv)"


lh = LopHoc("K20A")
for sv in lop:
    lh.them(sv)

print(f"   repr:        {lh}")
print(f"   len(lh):     {len(lh)}")
print(f"   lh[0]:       {lh[0]}")
print(f"   lh[-1]:      {lh[-1]}")
print(f"   lh[:2]:      {lh[:2]}")
print(f"   in:          {lop[0] in lh}")
print(f"   for:         {[sv.ten for sv in lh]}")
print(f"   sorted():    {sorted(lh)}   ← dùng cả __iter__ và __lt__")
print(f"   if lh:       {bool(lh)}     ← __len__ != 0 nên coi là True")

print("""
   Object của bạn giờ hoạt động y như list có sẵn của Python.
   Người dùng code của bạn không cần học API mới — họ đã biết len(), for, in.
   Đây là tinh thần Pythonic: hòa vào ngôn ngữ, đừng tạo thế giới riêng.""")


# ---------------------------------------------------------------
# 5. __add__ VÀ CÁC TOÁN TỬ
# ---------------------------------------------------------------
print("5. TOÁN TỬ")

from math import gcd


class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0")
        if mau < 0:
            tu, mau = -tu, -mau
        u = gcd(abs(tu), mau) or 1
        self.tu, self.mau = tu // u, mau // u        # tự rút gọn

    def __repr__(self):
        return f"{self.tu}/{self.mau}" if self.mau != 1 else str(self.tu)

    def __add__(self, k):
        return PhanSo(self.tu * k.mau + k.tu * self.mau, self.mau * k.mau)

    def __sub__(self, k):
        return PhanSo(self.tu * k.mau - k.tu * self.mau, self.mau * k.mau)

    def __mul__(self, k):
        return PhanSo(self.tu * k.tu, self.mau * k.mau)

    def __truediv__(self, k):
        return PhanSo(self.tu * k.mau, self.mau * k.tu)

    def __eq__(self, k):
        return (self.tu, self.mau) == (k.tu, k.mau)

    def __lt__(self, k):
        return self.tu * k.mau < k.tu * self.mau

    def __float__(self):
        return self.tu / self.mau


a, b = PhanSo(1, 2), PhanSo(1, 3)
print(f"   {a} + {b} = {a + b}")
print(f"   {a} - {b} = {a - b}")
print(f"   {a} * {b} = {a * b}")
print(f"   {a} / {b} = {a / b}")
print(f"   {a} == {PhanSo(2, 4)} → {a == PhanSo(2, 4)}   ← tự rút gọn rồi so sánh")
print(f"   {a} < {b} → {a < b}")
print(f"   sorted: {sorted([PhanSo(3, 4), a, b])}")
print(f"   float({a}) = {float(a)}")

print("""
   Danh sách dunder hay dùng:
     __init__ __str__ __repr__     khởi tạo và hiển thị
     __eq__ __hash__ __lt__        so sánh, sắp xếp, dùng trong set/dict
     __len__ __getitem__ __iter__  hoạt động như tập hợp
     __contains__                  toán tử in
     __add__ __sub__ __mul__       toán tử số học
     __enter__ __exit__            dùng được với `with`
     __call__                      gọi object như gọi hàm

   Đừng cài tất cả. Chỉ cài cái nào làm class của bạn tự nhiên hơn.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_17_dunder.py
#
# 1. class Tien(so_tien, don_vi): __add__ (chặn cộng khác đơn vị),
#    __str__, __eq__, __lt__
# 2. class Vector2D(x, y): __add__, __sub__, __mul__ (nhân số),
#    __abs__ (độ dài), __eq__, __repr__
# 3. class GioHang: __len__, __iter__, __contains__, __getitem__,
#    và __add__ để gộp hai giỏ hàng
# 4. class KhoangNgay(bat_dau, ket_thuc): __contains__ kiểm tra một ngày
#    có nằm trong khoảng, __len__ trả số ngày
