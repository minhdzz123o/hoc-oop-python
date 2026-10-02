"""
TUẦN 8 — @dataclass

Ở file 17 bạn thấy một class "chứa dữ liệu" cần viết rất nhiều code lặp:
__init__, __repr__, __eq__ — toàn bộ đều đoán được từ danh sách attribute.

@dataclass sinh những method đó tự động. Có từ Python 3.7.

Chạy: python 18_dataclass.py
"""

from dataclasses import dataclass, field, asdict, replace

# ---------------------------------------------------------------
# 1. SO SÁNH CODE
# ---------------------------------------------------------------
print("1. VIẾT TAY vs @dataclass")


class DiemTay:
    """Viết tay — 12 dòng cho một class chỉ chứa 2 số."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"DiemTay(x={self.x}, y={self.y})"

    def __eq__(self, k):
        if not isinstance(k, DiemTay):
            return NotImplemented
        return (self.x, self.y) == (k.x, k.y)


@dataclass
class Diem:
    """Cùng chức năng — 3 dòng."""
    x: float
    y: float


print(f"   viết tay:   {DiemTay(1, 2)}")
print(f"   dataclass:  {Diem(1, 2)}")
print(f"   __eq__ có sẵn: {Diem(1, 2) == Diem(1, 2)}")
print("   ← @dataclass sinh __init__, __repr__, __eq__ từ các annotation")


# ---------------------------------------------------------------
# 2. GIÁ TRỊ MẶC ĐỊNH VÀ field()
# ---------------------------------------------------------------
print("\n2. GIÁ TRỊ MẶC ĐỊNH")


@dataclass
class SanPham:
    ten: str
    gia: float
    so_luong: int = 1                            # mặc định như bình thường
    nhan: list[str] = field(default_factory=list)  # list → PHẢI dùng field()

    def tong(self):
        return self.gia * self.so_luong          # method viết như class thường


s1 = SanPham("Bàn", 1_200_000)
s2 = SanPham("Ghế", 350_000, 4, ["gỗ", "mới"])

print(f"   {s1}")
print(f"   {s2}")
print(f"   tổng s2: {s2.tong():,.0f}")

s1.nhan.append("khuyến mãi")
print(f"   nhãn s1: {s1.nhan}, nhãn s2: {s2.nhan}   ← độc lập")

print("""
   Vì sao list phải dùng field(default_factory=list)?
   Vì  nhan: list = []  sẽ mắc đúng cái bẫy mutable default ở file 02 và 06.
   @dataclass biết điều đó và BÁO LỖI nếu bạn viết vậy — hiếm khi một
   thư viện chặn giúp bạn cái bẫy này.""")

try:
    @dataclass
    class SaiCach:
        nhan: list = []
except ValueError as e:
    print(f"   thử viết nhan: list = [] → ValueError: {e}")


# ---------------------------------------------------------------
# 3. frozen=True — OBJECT KHÔNG ĐỔI ĐƯỢC
# ---------------------------------------------------------------
print("\n3. frozen=True (immutable)")


@dataclass(frozen=True)
class ToaDo:
    lat: float
    lon: float

    def khoang_cach_tho(self, k):
        return ((self.lat - k.lat) ** 2 + (self.lon - k.lon) ** 2) ** 0.5


hn = ToaDo(21.03, 105.85)
sg = ToaDo(10.82, 106.63)
print(f"   HN: {hn}")
print(f"   khoảng cách thô: {hn.khoang_cach_tho(sg):.2f}")

try:
    hn.lat = 0
except Exception as e:
    print(f"   gán hn.lat = 0 → {type(e).__name__}: {e}")

print(f"   frozen thì hashable, dùng được làm khóa dict: {bool({hn: 'Hà Nội'})}")

# replace() tạo BẢN MỚI với một field đổi — cách làm việc với immutable
hn2 = replace(hn, lat=21.05)
print(f"   replace(hn, lat=21.05) → {hn2}, bản gốc vẫn {hn}")

print("""
   Dùng frozen=True cho dữ liệu KHÔNG NÊN đổi sau khi tạo: toạ độ, tiền,
   một bản ghi lịch sử, cấu hình. Nó loại hẳn một lớp bug — "ai đã sửa
   object này?" — và cho bạn dùng object làm khóa dict / phần tử set.""")


# ---------------------------------------------------------------
# 4. order=True — SẮP XẾP TỰ ĐỘNG
# ---------------------------------------------------------------
print("4. order=True")


@dataclass(order=True)
class PhienBan:
    chinh: int
    phu: int
    sua: int


cac_ban = [PhienBan(1, 2, 3), PhienBan(1, 0, 0), PhienBan(2, 0, 0), PhienBan(1, 2, 0)]
print(f"   sorted: {sorted(cac_ban)}")
print(f"   max:    {max(cac_ban)}")
print("   ← so sánh theo thứ tự field khai báo, như tuple")


# ---------------------------------------------------------------
# 5. __post_init__ — VALIDATE
# ---------------------------------------------------------------
print("\n5. __post_init__ ĐỂ VALIDATE")

# @dataclass sinh __init__ hộ, nên muốn validate thì dùng __post_init__,
# nó chạy ngay sau __init__.


@dataclass
class NguoiDung:
    ten: str
    email: str
    tuoi: int

    def __post_init__(self):
        if not self.ten.strip():
            raise ValueError("Tên không được rỗng")
        if "@" not in self.email:
            raise ValueError(f"Email không hợp lệ: {self.email}")
        if not 0 < self.tuoi < 150:
            raise ValueError(f"Tuổi không hợp lệ: {self.tuoi}")
        self.ten = self.ten.strip()              # chuẩn hóa luôn
        self.email = self.email.lower()


u = NguoiDung("  Minh  ", "MINH@Example.COM", 20)
print(f"   {u}")

for args in [("", "a@b.com", 20), ("Lan", "sai", 20), ("Hùng", "h@b.com", 500)]:
    try:
        NguoiDung(*args)
    except ValueError as e:
        print(f"   bị chặn: {e}")


# ---------------------------------------------------------------
# 6. asdict() — CHUYỂN SANG DICT
# ---------------------------------------------------------------
print("\n6. asdict() ĐỂ LƯU JSON")

import json

print(f"   asdict(s2) = {asdict(s2)}")
print(f"   sang JSON:  {json.dumps(asdict(s2), ensure_ascii=False)}")
print("   ← rất tiện khi lưu file hoặc gửi qua API (dự án thư viện sẽ cần)")


# ---------------------------------------------------------------
# 7. KHI NÀO DÙNG @dataclass
# ---------------------------------------------------------------
print("\n7. KHI NÀO DÙNG")

print("""   DÙNG @dataclass khi class chủ yếu để CHỨA DỮ LIỆU:
     Diem, ToaDo, SanPham, CauHinh, một bản ghi đọc từ database

   KHÔNG dùng khi class chủ yếu là HÀNH VI:
     ThuVien, TroChoi, KetNoiDatabase — những class mà dữ liệu chỉ là
     phương tiện, phần chính là các method

   @dataclass vẫn dùng được với:
     - kế thừa  (@dataclass class Con(Cha))
     - abstract class
     - @property (nhưng hơi lằng nhằng, cân nhắc class thường)

   Lưu ý: @dataclass KHÔNG thay thế việc hiểu class. Nó chỉ bớt code lặp.
   Đó là lý do nó nằm ở tuần 8 chứ không phải tuần 3.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_18_dataclass.py
#
# 1. Viết lại class SinhVien, SanPham của các tuần trước bằng @dataclass
# 2. @dataclass(frozen=True) cho class Tien(so_tien, don_vi), thêm method
#    cong() trả về Tien MỚI thay vì sửa tại chỗ
# 3. @dataclass có __post_init__ cho class KhoangNgay(bat_dau, ket_thuc):
#    chặn nếu ket_thuc < bat_dau
# 4. @dataclass(order=True) cho class DiemThi, sắp xếp được theo điểm
# 5. Lấy một class bạn viết ở tuần 3-4, chuyển sang @dataclass.
#    Đếm xem bớt được bao nhiêu dòng.
