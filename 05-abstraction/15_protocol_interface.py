"""
TUẦN 7 — typing.Protocol: INTERFACE KHÔNG CẦN KẾ THỪA

Protocol là cách Python kết hợp hai thứ:
  - sự linh hoạt của duck typing (không cần kế thừa)
  - sự rõ ràng của interface (khai báo được "cần có method gì")

Protocol có từ Python 3.8. Nó là cách hiện đại để diễn đạt interface
trong Python.

Chạy: python 15_protocol_interface.py
"""

from typing import Protocol, runtime_checkable

# ---------------------------------------------------------------
# 1. KHAI BÁO MỘT PROTOCOL
# ---------------------------------------------------------------
print("1. PROTOCOL CƠ BẢN")


class CoTheGhi(Protocol):
    """Chỉ MÔ TẢ hình dạng cần có. Không ai phải kế thừa nó."""

    def ghi(self, dong: str) -> None:
        ...


# Ba class dưới đây KHÔNG kế thừa CoTheGhi, nhưng đều "khớp" với nó:


class GhiManHinh:
    def ghi(self, dong):
        print(f"      [màn hình] {dong}")


class GhiBoNho:
    def __init__(self):
        self.cac_dong = []

    def ghi(self, dong):
        self.cac_dong.append(dong)


class GhiCoTienTo:
    def __init__(self, tien_to):
        self.tien_to = tien_to
        self.cac_dong = []

    def ghi(self, dong):
        self.cac_dong.append(f"{self.tien_to}: {dong}")


def ghi_log(bo_ghi: CoTheGhi, cac_dong: list[str]) -> None:
    """Type hint nói rõ: tham số cần có method ghi(). Đọc code là hiểu."""
    for d in cac_dong:
        bo_ghi.ghi(d)


print("   ghi ra màn hình:")
ghi_log(GhiManHinh(), ["bắt đầu", "xong"])

bo_nho = GhiBoNho()
ghi_log(bo_nho, ["a", "b", "c"])
print(f"   ghi vào bộ nhớ: {bo_nho.cac_dong}")

tien_to = GhiCoTienTo("INFO")
ghi_log(tien_to, ["khởi động"])
print(f"   có tiền tố: {tien_to.cac_dong}")

print("""
   Protocol không chạy gì lúc runtime — nó là tài liệu cho người đọc
   và cho công cụ kiểm tra kiểu (mypy, pyright). Code vẫn là duck typing.""")


# ---------------------------------------------------------------
# 2. @runtime_checkable — kiểm tra được lúc chạy
# ---------------------------------------------------------------
print("2. runtime_checkable")


@runtime_checkable
class CoTheSoSanh(Protocol):
    def diem(self) -> float:
        ...


class SanPham:
    def __init__(self, ten, danh_gia):
        self.ten = ten
        self._danh_gia = danh_gia

    def diem(self):
        return self._danh_gia


class Chuoi:
    pass                      # không có method diem()


print(f"   SanPham khớp protocol? {isinstance(SanPham('A', 4.5), CoTheSoSanh)}")
print(f"   Chuoi   khớp protocol? {isinstance(Chuoi(), CoTheSoSanh)}")
print("   ← chỉ kiểm tra TÊN method có tồn tại, không kiểm tra tham số/kiểu trả về")


# ---------------------------------------------------------------
# 3. ABC vs PROTOCOL — CHỌN CÁI NÀO?
# ---------------------------------------------------------------
print("\n3. ABC vs PROTOCOL")

print("""
   ┌─────────────────────┬──────────────────────┬──────────────────────┐
   │                     │ abc.ABC              │ typing.Protocol      │
   ├─────────────────────┼──────────────────────┼──────────────────────┤
   │ phải kế thừa?       │ CÓ                   │ KHÔNG                │
   │ chứa code dùng chung│ ĐƯỢC                 │ không (chỉ mô tả)    │
   │ chứa dữ liệu/state  │ ĐƯỢC                 │ không                │
   │ bắt lỗi khi nào     │ lúc tạo object       │ lúc kiểm tra kiểu    │
   │ dùng với class của  │ chỉ class BẠN viết   │ cả class CỦA NGƯỜI   │
   │                     │                      │ KHÁC                 │
   └─────────────────────┴──────────────────────┴──────────────────────┘

   CHỌN abc.ABC khi:
   - bạn sở hữu toàn bộ cây class
   - có code/dữ liệu dùng chung muốn đặt ở lớp cha (như TaiLieu ở file 14)
   - muốn BẮT BUỘC lớp con cài đặt, chặn ngay lúc tạo object

   CHỌN Protocol khi:
   - cần làm việc với class bạn KHÔNG sửa được (thư viện ngoài)
   - chỉ muốn nói "tham số này cần có method X", không cần thừa kế gì
   - muốn dùng được object giả khi test, không muốn chúng phải kế thừa

   Nếu còn lưỡng lự: bắt đầu bằng duck typing thuần (không cần gì cả).
   Thêm Protocol khi muốn code dễ đọc hơn. Dùng ABC khi có code dùng chung.""")


# ---------------------------------------------------------------
# 4. VÍ DỤ: HAI PROTOCOL CHO HAI THỨ KHÔNG LIÊN QUAN
# ---------------------------------------------------------------
print("4. VÍ DỤ: CÙNG MỘT GIAO DIỆN CHO NHỮNG THỨ KHÁC HẲN NHAU")


class CoTheTraTien(Protocol):
    """Những thứ "trả được tiền" — vốn không có họ hàng gì với nhau."""

    def so_tien(self) -> float:
        ...

    def nguoi_nhan(self) -> str:
        ...


class NhanVien:
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def so_tien(self):
        return self.luong

    def nguoi_nhan(self):
        return self.ten


class HoaDonNhaCungCap:
    def __init__(self, cong_ty, tong, thue=0.1):
        self.cong_ty = cong_ty
        self.tong = tong
        self.thue = thue

    def so_tien(self):
        return self.tong * (1 + self.thue)

    def nguoi_nhan(self):
        return self.cong_ty


class HoanTienKhach:
    def __init__(self, khach, don_hang, tien):
        self.khach = khach
        self.don_hang = don_hang
        self.tien = tien

    def so_tien(self):
        return self.tien

    def nguoi_nhan(self):
        return f"{self.khach} (đơn {self.don_hang})"


def chay_dot_thanh_toan(cac_khoan: list[CoTheTraTien]) -> float:
    tong = 0.0
    for k in cac_khoan:
        tien = k.so_tien()
        tong += tien
        print(f"     {k.nguoi_nhan():28} {tien:>12,.0f}")
    return tong


khoan = [
    NhanVien("Minh", 15_000_000),
    HoaDonNhaCungCap("Công ty A", 8_000_000),
    HoanTienKhach("Lan", "DH123", 450_000),
]

print("   đợt thanh toán:")
tong = chay_dot_thanh_toan(khoan)
print(f"     {'TỔNG':28} {tong:>12,.0f}")

print("""
   Nhân viên, hóa đơn, hoàn tiền — ba thứ không có quan hệ is-a nào.
   Kế thừa chung một lớp cha "CoTheTraTien" sẽ rất vô lý.
   Protocol diễn đạt đúng điều ta cần: chúng chỉ TÌNH CỜ dùng chung được
   ở một chỗ, trong một bối cảnh.

   Đây là lý do interface/Protocol được dùng nhiều hơn kế thừa trong
   code thực tế.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_15_protocol.py
#
# 1. Protocol CoTheVe với method ve() -> str. Viết 3 class không liên quan
#    (Nut, BieuDo, BanDo) khớp protocol đó. Viết hàm render(cac_thu).
# 2. Protocol LuuTru với lay(khoa)/dat(khoa, gia_tri). Cài 2 phiên bản:
#    LuuTruRAM (dict) và LuuTruFile (json). Viết hàm dùng được cả hai.
# 3. Dùng @runtime_checkable + isinstance để lọc ra những object trong
#    một list hỗn hợp mà khớp protocol
# 4. Cho class TaiLieu ở file 14 (dùng ABC): nếu bạn phải tích hợp một class
#    tài liệu từ thư viện ngoài mà KHÔNG sửa được, bạn làm thế nào?
