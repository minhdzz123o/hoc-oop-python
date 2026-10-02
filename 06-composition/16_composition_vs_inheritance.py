"""
TUẦN 7 — COMPOSITION vs INHERITANCE

Nguyên tắc quan trọng nhất của OOP thực dụng:

    ƯU TIÊN COMPOSITION HƠN KẾ THỪA
    (Prefer composition over inheritance)

Trong code thực tế, composition được dùng nhiều hơn kế thừa rất nhiều.
Nhưng phần lớn tài liệu dạy OOP lại dành 80% thời lượng cho kế thừa.
Đó là lý do nhiều người học OOP xong viết code tệ.

Chạy: python 16_composition_vs_inheritance.py
"""

from abc import ABC, abstractmethod

# ---------------------------------------------------------------
# 1. HAI QUAN HỆ
# ---------------------------------------------------------------
print("1. IS-A vs HAS-A")

print("""   KẾ THỪA diễn đạt  IS-A  (là một loại của):
       XeMay LÀ MỘT XeCo
       Sach  LÀ MỘT TaiLieu

   COMPOSITION diễn đạt  HAS-A  (có một):
       Xe       CÓ MỘT DongCo
       ThuVien  CÓ NHIỀU TaiLieu
       DonHang  CÓ MỘT KhachHang và NHIỀU MonHang

   Phép thử: đọc to câu đó lên. Nghe vô lý thì chọn cái còn lại.""")


# ---------------------------------------------------------------
# 2. VÍ DỤ SAI — KẾ THỪA ĐỂ DÙNG LẠI CODE
# ---------------------------------------------------------------
print("2. CÁCH SAI")


class DongCo:
    def __init__(self, cong_suat):
        self.cong_suat = cong_suat
        self.dang_chay = False

    def khoi_dong(self):
        self.dang_chay = True
        return f"động cơ {self.cong_suat}HP đã khởi động"

    def tat(self):
        self.dang_chay = False


class XeSai(DongCo):              # SAI: "Xe LÀ MỘT động cơ"? Vô lý.
    def __init__(self, bien_so, cong_suat):
        super().__init__(cong_suat)
        self.bien_so = bien_so


x = XeSai("29A-12345", 150)
print(f"   {x.khoi_dong()}")
print(f"   nhưng x.cong_suat = {x.cong_suat} — xe có công suất? động cơ mới có")
print(f"   và isinstance(x, DongCo) = {isinstance(x, DongCo)} ← sai về ngữ nghĩa")

print("""
   Vấn đề thực sự xuất hiện khi:
   - Xe cần ĐỔI động cơ  → không thể, động cơ đã dính chặt vào class
   - Xe cần HAI động cơ   → không thể
   - Xe cần thêm Banh, HopSo → đa kế thừa, rắc rối tăng vọt
   - Mọi method của DongCo bị lộ ra ngoài qua Xe, kể cả cái không liên quan""")


# ---------------------------------------------------------------
# 3. CÁCH ĐÚNG — COMPOSITION
# ---------------------------------------------------------------
print("3. CÁCH ĐÚNG")


class Banh:
    def __init__(self, so_luong, duong_kinh):
        self.so_luong = so_luong
        self.duong_kinh = duong_kinh

    def mo_ta(self):
        return f"{self.so_luong} bánh {self.duong_kinh}inch"


class HopSo:
    def __init__(self, so_cap, tu_dong=False):
        self.so_cap = so_cap
        self.tu_dong = tu_dong
        self.cap_hien_tai = 0

    def mo_ta(self):
        kieu = "tự động" if self.tu_dong else "số sàn"
        return f"{self.so_cap} cấp {kieu}"


class Xe:
    """Xe CÓ động cơ, CÓ bánh, CÓ hộp số."""

    def __init__(self, bien_so, dong_co, banh, hop_so):
        self.bien_so = bien_so
        self.dong_co = dong_co          # composition
        self.banh = banh
        self.hop_so = hop_so

    def khoi_dong(self):
        """Xe CHỌN những gì nó muốn lộ ra ngoài — lợi ích lớn của composition."""
        return f"Xe {self.bien_so}: {self.dong_co.khoi_dong()}"

    def thay_dong_co(self, dong_co_moi):
        """Việc này KHÔNG LÀM ĐƯỢC với kế thừa."""
        cu = self.dong_co.cong_suat
        self.dong_co = dong_co_moi
        return f"đã thay động cơ {cu}HP sang {dong_co_moi.cong_suat}HP"

    def thong_tin(self):
        return (f"Xe {self.bien_so}: {self.dong_co.cong_suat}HP, "
                f"{self.banh.mo_ta()}, {self.hop_so.mo_ta()}")


xe = Xe("29A-12345", DongCo(150), Banh(4, 17), HopSo(6, tu_dong=True))
print(f"   {xe.thong_tin()}")
print(f"   {xe.khoi_dong()}")
print(f"   {xe.thay_dong_co(DongCo(300))}")
print(f"   {xe.thong_tin()}")

# Xe không bị lộ method tat() của động cơ nếu Xe không muốn:
print(f"   xe có method tat()? {hasattr(xe, 'tat')} ← Xe tự kiểm soát giao diện")

xe_dien = Xe("30E-99999", DongCo(400), Banh(4, 19), HopSo(1, tu_dong=True))
print(f"   {xe_dien.thong_tin()}")


# ---------------------------------------------------------------
# 4. COMPOSITION LÀM ĐƯỢC THỨ KẾ THỪA KHÔNG LÀM ĐƯỢC
# ---------------------------------------------------------------
print("\n4. THAY ĐỔI HÀNH VI LÚC CHẠY")


class TinhPhiThuong:
    def tinh(self, km):
        return km * 10_000


class TinhPhiGioCaoDiem:
    def tinh(self, km):
        return km * 10_000 * 1.5


class TinhPhiKhuyenMai:
    def __init__(self, giam):
        self.giam = giam

    def tinh(self, km):
        return km * 10_000 * (1 - self.giam)


class CuocXe:
    def __init__(self, km, cach_tinh=None):
        self.km = km
        self.cach_tinh = cach_tinh or TinhPhiThuong()      # composition

    def doi_cach_tinh(self, cach_moi):
        self.cach_tinh = cach_moi                          # đổi LÚC CHẠY

    def gia(self):
        return self.cach_tinh.tinh(self.km)


c = CuocXe(12)
print(f"   giá thường:      {c.gia():>10,.0f}")

c.doi_cach_tinh(TinhPhiGioCaoDiem())
print(f"   giờ cao điểm:    {c.gia():>10,.0f}")

c.doi_cach_tinh(TinhPhiKhuyenMai(0.3))
print(f"   khuyến mãi 30%:  {c.gia():>10,.0f}")

print("""
   Với kế thừa bạn sẽ cần CuocXeThuong, CuocXeCaoDiem, CuocXeKhuyenMai —
   và một chuyến xe KHÔNG THỂ đổi cách tính giữa đường, vì class của một
   object là cố định sau khi tạo.

   Với composition: chỉ cần gán lại một attribute.
   Đây chính là Strategy pattern — pattern được dùng nhiều nhất trong thực tế.""")


# ---------------------------------------------------------------
# 5. KHI NÀO KẾ THỪA VẪN ĐÚNG
# ---------------------------------------------------------------
print("5. KẾ THỪA VẪN CÓ CHỖ DÙNG")

print("""   Đừng hiểu "ưu tiên composition" thành "cấm kế thừa". Kế thừa đúng khi:

   1. Quan hệ is-a thật sự và BẤT BIẾN
      Sach LÀ MỘT TaiLieu — một quyển sách không bao giờ thành cái DVD

   2. Lớp cha có code dùng chung đáng kể, lớp con chỉ khác vài điểm
      TaiLieu ở file 14: cho_muon()/tra() dùng chung, chỉ khác so_ngay_muon()

   3. Bạn cần đa hình qua một cây class mình sở hữu hoàn toàn
      Hinh → HinhTron, HinhVuong ở file 12

   Quy tắc thực dụng:
   - cây kế thừa sâu tối đa 2 tầng; sâu hơn thì xem lại thiết kế
   - thấy mình kế thừa CHỈ ĐỂ dùng lại code → chuyển sang composition
   - thấy mình override method để vô hiệu hóa nó → kế thừa sai
   - lưỡng lự → chọn composition, vì nó dễ sửa về sau hơn

   Câu hỏi quyết định: "X CÓ THỂ ĐỔI THÀNH loại khác không?"
     Động cơ của xe có thể đổi    → composition
     Sách không thể thành DVD     → kế thừa""")


# ---------------------------------------------------------------
# 6. VÍ DỤ TỔNG HỢP: CẢ HAI CÙNG DÙNG
# ---------------------------------------------------------------
print("6. DÙNG CẢ HAI ĐÚNG CHỖ")


class TaiLieu(ABC):                        # KẾ THỪA: is-a, bất biến
    def __init__(self, tieu_de):
        self.tieu_de = tieu_de

    @abstractmethod
    def so_ngay_muon(self): ...


class Sach(TaiLieu):
    def so_ngay_muon(self):
        return 30


class DiaDVD(TaiLieu):
    def so_ngay_muon(self):
        return 7


class ThanhVien:
    def __init__(self, ten, toi_da=3):
        self.ten = ten
        self.toi_da = toi_da
        self.dang_muon = []                # COMPOSITION: has-a


class ThuVien:
    def __init__(self, ten):
        self.ten = ten
        self.kho = []                      # COMPOSITION: has-many
        self.thanh_vien = []

    def them_tai_lieu(self, tl):
        self.kho.append(tl)

    def them_thanh_vien(self, tv):
        self.thanh_vien.append(tv)

    def cho_muon(self, tv, tl):
        if len(tv.dang_muon) >= tv.toi_da:
            raise ValueError(f"{tv.ten} đã mượn tối đa {tv.toi_da} tài liệu")
        if tl not in self.kho:
            raise ValueError(f"{tl.tieu_de} không có trong kho")
        self.kho.remove(tl)
        tv.dang_muon.append(tl)
        return f"{tv.ten} mượn [{tl.tieu_de}] trong {tl.so_ngay_muon()} ngày"


tv_lib = ThuVien("Thư viện Quốc gia")
s1, s2, d1 = Sach("Clean Code"), Sach("Refactoring"), DiaDVD("Inception")
for tl in (s1, s2, d1):
    tv_lib.them_tai_lieu(tl)

minh = ThanhVien("Minh", toi_da=2)
tv_lib.them_thanh_vien(minh)

print(f"   {tv_lib.cho_muon(minh, s1)}")
print(f"   {tv_lib.cho_muon(minh, d1)}")
try:
    tv_lib.cho_muon(minh, s2)
except ValueError as e:
    print(f"   bị chặn: {e}")

print(f"   còn trong kho: {[t.tieu_de for t in tv_lib.kho]}")

print("""
   Thiết kế trên dùng:
     KẾ THỪA     cho TaiLieu sang Sach/DiaDVD  (is-a, bất biến, có đa hình)
     COMPOSITION cho ThuVien CÓ kho            (has-a, số lượng thay đổi)
                 ThanhVien CÓ dang_muon

   Đây là tỷ lệ bình thường trong code thật: ít kế thừa, nhiều composition.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_16_composition.py
#
# 1. class MayTinh gồm CPU, RAM, OCung (composition). Cho phép nang_cap_ram().
#    Viết thong_tin() in cấu hình đầy đủ.
# 2. Cho các cặp sau, chọn kế thừa hay composition và GIẢI THÍCH:
#    a) NguoiDung / TaiKhoanAdmin        b) DonHang / DiaChiGiaoHang
#    c) Hinh / HinhTron                  d) NhaHang / ThucDon
#    e) Logger / LoggerGhiFile           f) GioHang / MaGiamGia
# 3. Viết class TroChoi dùng composition cho cách tính điểm: TinhDiemThuong,
#    TinhDiemNhanDoi, TinhDiemTheoThoiGian — đổi được giữa game
# 4. Lấy một bài kế thừa bạn đã làm ở tuần 5, viết lại bằng composition.
#    So sánh: cách nào dễ thêm tính năng mới hơn?
