"""
TUẦN 5 — INHERITANCE (KẾ THỪA)

Kế thừa diễn đạt quan hệ "is-a" (là một loại của):
    NhanVienFullTime LÀ MỘT NhanVien
    Cho LÀ MỘT DongVat

Cảnh báo trước khi học: kế thừa là thứ bị LẠM DỤNG nhiều nhất trong OOP.
Học nó để hiểu code người khác và để dùng đúng chỗ — không phải để dùng mọi chỗ.
Tuần 7 sẽ cho bạn công cụ tốt hơn trong phần lớn tình huống (composition).

Chạy: python 10_ke_thua_super.py
"""

# ---------------------------------------------------------------
# 1. KẾ THỪA CƠ BẢN
# ---------------------------------------------------------------
print("1. KẾ THỪA CƠ BẢN")


class NhanVien:
    """Lớp CHA (base class / superclass)."""

    def __init__(self, ten, ma_nv):
        self.ten = ten
        self.ma_nv = ma_nv

    def thong_tin(self):
        return f"{self.ten} (mã {self.ma_nv})"

    def luong(self):
        return 0


class NhanVienFullTime(NhanVien):          # ← kế thừa: class Con(Cha)
    def __init__(self, ten, ma_nv, luong_thang):
        super().__init__(ten, ma_nv)       # gọi __init__ của CHA trước
        self.luong_thang = luong_thang     # rồi thêm phần RIÊNG của con

    def luong(self):
        return self.luong_thang


nv = NhanVienFullTime("Minh", "NV001", 15_000_000)
print(f"   {nv.thong_tin()}")              # method kế thừa từ cha
print(f"   lương: {nv.luong():,}")         # method của riêng con
print(f"   là NhanVien? {isinstance(nv, NhanVien)}   ← quan hệ is-a")


# ---------------------------------------------------------------
# 2. BẪY: QUÊN super().__init__()
# ---------------------------------------------------------------
print("\n2. BẪY: QUÊN super().__init__()")


class ConQuen(NhanVien):
    def __init__(self, ten, ma_nv, thuong):
        # QUÊN gọi super().__init__(ten, ma_nv)
        self.thuong = thuong


c = ConQuen("Lan", "NV002", 1000)
try:
    print(c.thong_tin())
except AttributeError as e:
    print(f"   lỗi: {e}")
    print("   ← self.ten chưa bao giờ được gán, vì __init__ của cha không chạy")

print("""
   Quy tắc: __init__ của con GHI ĐÈ của cha. Nếu con có __init__ riêng thì
   PHẢI tự gọi super().__init__(...) — Python không gọi hộ.

   Nếu con không cần thêm gì, cứ bỏ hẳn __init__ đi, con sẽ dùng của cha.""")


# ---------------------------------------------------------------
# 3. CÂY KẾ THỪA ĐẦY ĐỦ
# ---------------------------------------------------------------
print("3. CÂY KẾ THỪA")


class NhanVienPartTime(NhanVien):
    GIO_TOI_DA = 160

    def __init__(self, ten, ma_nv, luong_gio, so_gio):
        super().__init__(ten, ma_nv)
        if so_gio > NhanVienPartTime.GIO_TOI_DA:
            raise ValueError(f"Part-time không quá {NhanVienPartTime.GIO_TOI_DA} giờ")
        self.luong_gio = luong_gio
        self.so_gio = so_gio

    def luong(self):
        return self.luong_gio * self.so_gio


class QuanLy(NhanVienFullTime):            # kế thừa 2 tầng
    def __init__(self, ten, ma_nv, luong_thang, so_nguoi_quan_ly):
        super().__init__(ten, ma_nv, luong_thang)
        self.so_nguoi_quan_ly = so_nguoi_quan_ly

    def luong(self):
        # Gọi cách tính của CHA rồi cộng thêm — cách dùng super() rất hay gặp
        return super().luong() + self.so_nguoi_quan_ly * 500_000


nhan_su = [
    NhanVienFullTime("Minh", "NV001", 15_000_000),
    NhanVienPartTime("Lan", "NV002", 80_000, 100),
    QuanLy("Hùng", "NV003", 25_000_000, 6),
]

for n in nhan_su:
    print(f"   {n.thong_tin():22} {n.luong():>12,}")

print(f"   {'TỔNG QUỸ LƯƠNG':22} {sum(n.luong() for n in nhan_su):>12,}")
print("   ← một vòng lặp xử lý được cả 3 loại. Đây là ĐA HÌNH, chủ đề tuần 6.")


# ---------------------------------------------------------------
# 4. MRO — THỨ TỰ TÌM METHOD
# ---------------------------------------------------------------
print("\n4. MRO (Method Resolution Order)")

print("   Khi gọi q.luong(), Python tìm theo thứ tự:")
for i, cls in enumerate(QuanLy.__mro__, 1):
    print(f"     {i}. {cls.__name__}")

print("""
   Tìm thấy ở đâu thì dùng cái đó, dừng luôn. Nên QuanLy.luong() thắng
   NhanVienFullTime.luong().

   Hiện tại chỉ cần biết MRO tồn tại. Nó thành quan trọng khi gặp đa kế thừa
   (class Con(ChaA, ChaB)) — thứ bạn nên TRÁNH khi mới học, vì rất dễ gây
   rắc rối khó debug.""")


# ---------------------------------------------------------------
# 5. KHI NÀO KẾ THỪA LÀ SAI
# ---------------------------------------------------------------
print("5. KHI NÀO KẾ THỪA LÀ SAI")

print("""   Phép thử: đọc to câu "Con LÀ MỘT Cha". Nghe vô lý thì đừng kế thừa.

     NhanVienFullTime LÀ MỘT NhanVien   → hợp lý, kế thừa đúng
     Xe LÀ MỘT DongCo                   → vô lý! Xe CÓ một động cơ
     NguoiDung LÀ MỘT KetNoiDatabase    → vô lý! Nó DÙNG database

   Dấu hiệu bạn đang lạm dụng kế thừa:
   - cây sâu quá 2-3 tầng
   - lớp con phải ghi đè method của cha để "vô hiệu hóa" nó
   - lớp con chỉ dùng 1-2 trong 10 method của cha
   - bạn kế thừa chỉ để DÙNG LẠI CODE, không phải vì quan hệ is-a

   Ví dụ kinh điển của kế thừa sai:
       class HinhVuong(HinhChuNhat): ...
   Nghe rất hợp lý về mặt toán học, nhưng nếu HinhChuNhat cho đổi rộng/cao
   riêng lẻ thì HinhVuong không thể giữ được tính chất của nó. Google
   "Liskov Substitution Principle" khi bạn học tới SOLID.

   Tuần 7 sẽ cho giải pháp: COMPOSITION.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_10_ke_thua.py
#
# 1. class DongVat(ten) với keu() và di_chuyen().
#    Tạo Cho, Meo, Chim, Ca kế thừa, mỗi loài keu() và di_chuyen() khác nhau
# 2. class TaiKhoan(chu, so_du) → TaiKhoanTietKiem (có lai_suat, tinh_lai())
#    và TaiKhoanThanhToan (có phi_giao_dich, rut() trừ thêm phí)
# 3. class Xe(bien_so) → XeMay, XeTai với phi_cau_duong() khác nhau
# 4. Viết một class con CỐ TÌNH quên super().__init__(), chạy thử, đọc lỗi
# 5. Tìm trong 3 bài trên: có chỗ nào đáng lẽ nên dùng composition không?
