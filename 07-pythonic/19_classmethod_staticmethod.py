"""
TUẦN 8 — @classmethod VÀ @staticmethod

Ba loại method trong một class:

    def thuong(self):       — nhận OBJECT, dùng dữ liệu của object
    @classmethod            — nhận CLASS, không cần object nào
    @staticmethod           — không nhận gì, chỉ là hàm đặt trong class

Chạy: python 19_classmethod_staticmethod.py
"""

# ---------------------------------------------------------------
# 1. BA LOẠI METHOD
# ---------------------------------------------------------------
print("1. BA LOẠI METHOD")


class ViDu:
    bien_class = "dùng chung"

    def __init__(self, gia_tri):
        self.gia_tri = gia_tri

    def method_thuong(self):
        return f"thấy object: gia_tri = {self.gia_tri}"

    @classmethod
    def method_class(cls):
        """cls là CLASS, không phải object. Không truy cập được self.gia_tri."""
        return f"thấy class: {cls.__name__}, bien_class = {cls.bien_class}"

    @staticmethod
    def method_static(x, y):
        """Không nhận self hay cls. Chỉ là hàm được đặt trong class."""
        return f"chỉ biết tham số: {x} + {y} = {x + y}"


v = ViDu(42)
print(f"   {v.method_thuong()}")
print(f"   {ViDu.method_class()}        ← gọi qua CLASS, không cần object")
print(f"   {ViDu.method_static(2, 3)}")


# ---------------------------------------------------------------
# 2. @classmethod LÀM CONSTRUCTOR THAY THẾ — dùng nhiều nhất
# ---------------------------------------------------------------
print("\n2. CONSTRUCTOR THAY THẾ (quan trọng nhất)")

# Python chỉ cho MỘT __init__. Muốn nhiều cách tạo object thì dùng classmethod.


class NgayThang:
    def __init__(self, ngay, thang, nam):
        if not 1 <= thang <= 12:
            raise ValueError(f"Tháng không hợp lệ: {thang}")
        if not 1 <= ngay <= 31:
            raise ValueError(f"Ngày không hợp lệ: {ngay}")
        self.ngay, self.thang, self.nam = ngay, thang, nam

    def __repr__(self):
        return f"{self.ngay:02d}/{self.thang:02d}/{self.nam}"

    # --- nhiều cách tạo object, cùng một __init__ ---

    @classmethod
    def tu_chuoi(cls, s):
        """NgayThang.tu_chuoi('02/10/2026')"""
        ngay, thang, nam = (int(x) for x in s.split("/"))
        return cls(ngay, thang, nam)          # cls(...) chính là gọi __init__

    @classmethod
    def tu_iso(cls, s):
        """NgayThang.tu_iso('2026-10-02')"""
        nam, thang, ngay = (int(x) for x in s.split("-"))
        return cls(ngay, thang, nam)

    @classmethod
    def hom_nay(cls):
        import datetime
        d = datetime.date.today()
        return cls(d.day, d.month, d.year)


print(f"   NgayThang(2, 10, 2026)            → {NgayThang(2, 10, 2026)}")
print(f"   NgayThang.tu_chuoi('02/10/2026')  → {NgayThang.tu_chuoi('02/10/2026')}")
print(f"   NgayThang.tu_iso('2026-10-02')    → {NgayThang.tu_iso('2026-10-02')}")
print(f"   NgayThang.hom_nay()               → {NgayThang.hom_nay()}")

print("""
   Tên method nói rõ nó nhận gì. So với cách tệ là nhồi mọi thứ vào __init__
   rồi đoán kiểu đầu vào:

       def __init__(self, x):          # ĐỪNG
           if isinstance(x, str):
               if "/" in x: ...
               elif "-" in x: ...
           elif isinstance(x, tuple): ...

   Một __init__ rõ ràng + nhiều classmethod là cách đúng.""")


# ---------------------------------------------------------------
# 3. cls GIÚP classmethod HOẠT ĐỘNG VỚI LỚP CON
# ---------------------------------------------------------------
print("3. VÌ SAO DÙNG cls CHỨ KHÔNG VIẾT TÊN CLASS")


class TaiLieu:
    def __init__(self, tieu_de):
        self.tieu_de = tieu_de

    @classmethod
    def tu_dong_csv(cls, dong):
        """cls = class THẬT SỰ được gọi, nên lớp con tự động đúng."""
        return cls(dong.split(",")[0])

    def __repr__(self):
        return f"{type(self).__name__}({self.tieu_de!r})"


class Sach(TaiLieu):
    pass


class DiaDVD(TaiLieu):
    pass


print(f"   TaiLieu.tu_dong_csv('A,...')  → {TaiLieu.tu_dong_csv('A,2020')}")
print(f"   Sach.tu_dong_csv('B,...')     → {Sach.tu_dong_csv('B,2021')}")
print(f"   DiaDVD.tu_dong_csv('C,...')   → {DiaDVD.tu_dong_csv('C,2022')}")
print("   ← một method, ba class. Nếu viết return TaiLieu(...) thì cả ba")
print("     đều trả về TaiLieu, lớp con mất tác dụng.")


# ---------------------------------------------------------------
# 4. @staticmethod — DÙNG ÍT, VÀ CÓ LÝ DO
# ---------------------------------------------------------------
print("\n4. @staticmethod")


class TinhToan:
    @staticmethod
    def la_nam_nhuan(nam):
        return nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)

    @staticmethod
    def so_ngay_trong_thang(thang, nam):
        if thang == 2:
            return 29 if TinhToan.la_nam_nhuan(nam) else 28
        return 30 if thang in (4, 6, 9, 11) else 31


print(f"   2024 nhuận? {TinhToan.la_nam_nhuan(2024)}")
print(f"   2100 nhuận? {TinhToan.la_nam_nhuan(2100)}  ← chia hết 100, không hết 400")
print(f"   tháng 2/2024 có {TinhToan.so_ngay_trong_thang(2, 2024)} ngày")

print("""
   @staticmethod chỉ là hàm thường được đặt trong class để GOM NHÓM.
   Dấu hiệu bạn nên cân nhắc: nếu class của bạn CHỈ CÓ staticmethod,
   thì nó không phải class — hãy dùng một module (file .py) với các hàm
   thường. Python không bắt mọi thứ phải nằm trong class như Java.

   Dùng @staticmethod khi: hàm liên quan logic tới class, nhưng không cần
   dữ liệu của object hay của class. Ví dụ hàm validate, hàm tính toán phụ.""")


# ---------------------------------------------------------------
# 5. TỔNG HỢP: MỘT CLASS DÙNG CẢ BA
# ---------------------------------------------------------------
print("5. VÍ DỤ TỔNG HỢP")


class Tien:
    TY_GIA = {"VND": 1.0, "USD": 25_000.0, "EUR": 27_000.0}

    def __init__(self, so_tien, don_vi="VND"):
        if don_vi not in Tien.TY_GIA:
            raise ValueError(f"Không hỗ trợ đơn vị {don_vi}")
        if not Tien.hop_le(so_tien):
            raise ValueError(f"Số tiền không hợp lệ: {so_tien}")
        self.so_tien = so_tien
        self.don_vi = don_vi

    # --- static: kiểm tra thuần, không cần self/cls ---
    @staticmethod
    def hop_le(so_tien):
        return isinstance(so_tien, (int, float)) and so_tien >= 0

    # --- classmethod: cách tạo object thay thế ---
    @classmethod
    def tu_chuoi(cls, s):
        """Tien.tu_chuoi('100 USD')"""
        phan = s.split()
        return cls(float(phan[0]), phan[1] if len(phan) > 1 else "VND")

    @classmethod
    def khong(cls, don_vi="VND"):
        return cls(0, don_vi)

    @classmethod
    def cac_don_vi(cls):
        return list(cls.TY_GIA)

    # --- method thường: cần dữ liệu của object ---
    def sang_vnd(self):
        return self.so_tien * Tien.TY_GIA[self.don_vi]

    def doi_sang(self, don_vi_moi):
        return Tien(self.sang_vnd() / Tien.TY_GIA[don_vi_moi], don_vi_moi)

    def __repr__(self):
        return f"{self.so_tien:,.2f} {self.don_vi}"

    def __add__(self, k):
        """Cộng được cả khi khác đơn vị — quy về đơn vị của bên trái."""
        tong_vnd = self.sang_vnd() + k.sang_vnd()
        return Tien(tong_vnd / Tien.TY_GIA[self.don_vi], self.don_vi)


print(f"   các đơn vị:              {Tien.cac_don_vi()}")
print(f"   Tien.tu_chuoi('100 USD') → {Tien.tu_chuoi('100 USD')}")
print(f"   Tien.khong('EUR')        → {Tien.khong('EUR')}")

a = Tien(100, "USD")
b = Tien(50, "EUR")
print(f"   {a} sang VND             → {a.sang_vnd():,.0f}")
print(f"   {a} sang EUR             → {a.doi_sang('EUR')}")
print(f"   {a} + {b}  → {a + b}")

try:
    Tien(-50)
except ValueError as e:
    print(f"   Tien(-50) bị chặn: {e}")

print("""
   Nhìn lại class Tien: nó dùng gần hết những gì bạn học 8 tuần qua —
   class attribute (TY_GIA), validate trong __init__ (tuần 3), staticmethod,
   classmethod làm constructor thay thế, method thường, và dunder
   __repr__/__add__ (file 17).

   Bạn đã học hết phần cốt lõi của OOP Python. Giờ là lúc làm dự án.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_19_classmethod.py
#
# 1. class NhietDo: thêm classmethod tu_fahrenheit(f) và tu_kelvin(k)
# 2. class SinhVien: classmethod tu_dong_csv("Minh,8.5,K20") và
#    tu_dict({"ten": ..., "diem": ...})
# 3. class CauHinh: classmethod mac_dinh() trả về cấu hình chuẩn,
#    tu_file(duong_dan) đọc từ JSON
# 4. class ThoiLuong(giay): classmethod tu_phut(p), tu_gio(g), tu_chuoi("1:30:00")
#    và staticmethod hop_le(chuoi)
# 5. Tìm trong code bạn đã viết: có class nào chỉ gồm staticmethod không?
#    Nếu có, chuyển nó thành module hàm thường.
