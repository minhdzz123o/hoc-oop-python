"""
TUẦN 3 — __init__ VÀ self

Hai thứ gây bối rối nhất cho người mới. File này giải thích kỹ.

Chạy: python 06_constructor_self.py
"""

# ---------------------------------------------------------------
# 1. self LÀ GÌ?
# ---------------------------------------------------------------
print("1. self LÀ GÌ")


class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hien_self(self):
        return f"self trỏ tới object ở địa chỉ {id(self)}"


p = Diem(1, 2)
print(f"   {p.hien_self()}")
print(f"   id(p) = {id(p)}   ← cùng một số")

# self KHÔNG phải từ khóa. Nó chỉ là tên tham số đầu tiên theo quy ước.
# Python tự truyền object vào vị trí đó. Hai dòng sau tương đương:
print(f"   p.hien_self()      → {p.hien_self()[:20]}...")
print(f"   Diem.hien_self(p)  → {Diem.hien_self(p)[:20]}...")
print("   ← p.method() thực chất là Class.method(p)")

# Vì vậy QUÊN self trong định nghĩa method là lỗi rất hay gặp:
#     def tinh():            SAI  → TypeError khi gọi
#     def tinh(self):        ĐÚNG


# ---------------------------------------------------------------
# 2. __init__ KHÔNG PHẢI "HÀM TẠO OBJECT"
# ---------------------------------------------------------------
print("\n2. __init__ LÀM GÌ")

print("""   Khi bạn viết  p = Diem(1, 2)  Python làm 2 việc:
     1. tạo một object rỗng
     2. gọi __init__(object_đó, 1, 2) để điền giá trị vào

   Nên __init__ không return gì. Nếu bạn viết `return self` trong đó,
   Python sẽ báo lỗi.""")


# ---------------------------------------------------------------
# 3. THAM SỐ MẶC ĐỊNH TRONG __init__
# ---------------------------------------------------------------
print("\n3. THAM SỐ MẶC ĐỊNH")


class GioHang:
    def __init__(self, chu_hang, mon=None):     # ĐÚNG: dùng None, không dùng []
        self.chu_hang = chu_hang
        self.mon = mon if mon is not None else []

    def them(self, ten):
        self.mon.append(ten)


g1 = GioHang("Minh")
g2 = GioHang("Lan")
g1.them("Táo")
g2.them("Cam")
print(f"   g1: {g1.mon}, g2: {g2.mon}   ← độc lập, đúng")


class GioHangSai:
    def __init__(self, chu_hang, mon=[]):       # SAI: đây là cái bẫy
        self.chu_hang = chu_hang
        self.mon = mon

    def them(self, ten):
        self.mon.append(ten)


s1 = GioHangSai("Minh")
s2 = GioHangSai("Lan")
s1.them("Táo")
s2.them("Cam")
print(f"   s1: {s1.mon}, s2: {s2.mon}   ← DÙNG CHUNG LIST, sai")
print("   ← chính là bẫy ở file 02_ham.py mục 5, nay nằm trong __init__")


# ---------------------------------------------------------------
# 4. __init__ NÊN BẢO ĐẢM OBJECT HỢP LỆ NGAY TỪ ĐẦU
# ---------------------------------------------------------------
print("\n4. VALIDATE TRONG __init__")

# Nguyên tắc: một object vừa tạo ra phải ở trạng thái HỢP LỆ.
# Đừng để người dùng tạo được object vô nghĩa rồi mới sửa sau.


class NguoiDung:
    def __init__(self, ten, email, tuoi):
        if not ten.strip():
            raise ValueError("Tên không được rỗng")
        if "@" not in email:
            raise ValueError(f"Email không hợp lệ: {email}")
        if not 0 < tuoi < 150:
            raise ValueError(f"Tuổi không hợp lệ: {tuoi}")

        self.ten = ten.strip()
        self.email = email.lower()
        self.tuoi = tuoi


u = NguoiDung("  Minh  ", "MINH@Example.COM", 20)
print(f"   tên đã trim: [{u.ten}]")
print(f"   email đã chuẩn hóa: {u.email}")

xau = [("", "a@b.com", 20), ("Lan", "khong-co-a", 20), ("Hùng", "h@b.com", 200)]
for ten, email, tuoi in xau:
    try:
        NguoiDung(ten, email, tuoi)
    except ValueError as e:
        print(f"   bị chặn: {e}")


# ---------------------------------------------------------------
# 5. OBJECT CHỨA OBJECT KHÁC — nhìn trước tuần 7
# ---------------------------------------------------------------
print("\n5. OBJECT CHỨA OBJECT")


class DiaChi:
    def __init__(self, duong, thanh_pho):
        self.duong = duong
        self.thanh_pho = thanh_pho

    def mo_ta(self):
        return f"{self.duong}, {self.thanh_pho}"


class KhachHang:
    def __init__(self, ten, dia_chi):
        self.ten = ten
        self.dia_chi = dia_chi        # attribute là một OBJECT, không phải chuỗi

    def thong_tin(self):
        return f"{self.ten} — {self.dia_chi.mo_ta()}"


kh = KhachHang("Minh", DiaChi("12 Lê Lợi", "Hà Nội"))
print(f"   {kh.thong_tin()}")
print("   ← đây là COMPOSITION, chủ đề chính của tuần 7")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_06_init.py
#
# 1. class NgayThang(ngay, thang, nam) — __init__ chặn ngày/tháng vô lý
#    (tháng 1-12, ngày 1-31; chưa cần xử lý tháng 2 năm nhuận)
# 2. class MatKhau(chuoi) — chặn nếu dưới 8 ký tự hoặc không có chữ số
# 3. class DanhSachViec(ten, viec=None) — làm đúng, không mắc bẫy mutable
# 4. Tự trả lời: vì sao nên validate trong __init__ thay vì để người dùng
#    tạo object rồi gán attribute sau?
