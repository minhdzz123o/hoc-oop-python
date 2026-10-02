"""
TUẦN 7 — ABSTRACT CLASS (abc.ABC)

Ở file 12 ta viết:

    def dien_tich(self):
        raise NotImplementedError

Cách đó có vấn đề: lỗi chỉ xảy ra khi ai đó GỌI method, có thể rất muộn.
abc.ABC chặn sớm hơn — ngay lúc TẠO object.

Chạy: python 14_abstract_class.py
"""

from abc import ABC, abstractmethod

# ---------------------------------------------------------------
# 1. VẤN ĐỀ CỦA NotImplementedError
# ---------------------------------------------------------------
print("1. VẤN ĐỀ CỦA NotImplementedError")


class HinhCu:
    def dien_tich(self):
        raise NotImplementedError


class HinhThieu(HinhCu):
    pass                                 # quên cài đặt dien_tich()


h = HinhThieu()                          # tạo được bình thường!
print(f"   tạo HinhThieu() → OK, không có lỗi gì")
try:
    h.dien_tich()
except NotImplementedError:
    print("   nhưng gọi dien_tich() → NotImplementedError")
    print("   ← lỗi xảy ra MUỘN, có thể sau khi object đã đi qua nửa hệ thống")


# ---------------------------------------------------------------
# 2. abc.ABC CHẶN NGAY LÚC TẠO OBJECT
# ---------------------------------------------------------------
print("\n2. abc.ABC")


class Hinh(ABC):                         # kế thừa ABC → class trừu tượng
    def __init__(self, ten):
        self.ten = ten

    @abstractmethod
    def dien_tich(self):
        """Lớp con BẮT BUỘC phải cài đặt."""

    @abstractmethod
    def chu_vi(self):
        """Lớp con BẮT BUỘC phải cài đặt."""

    # Method thường vẫn viết được bình thường — và dùng được method abstract
    def mo_ta(self):
        return f"{self.ten}: S={self.dien_tich():.2f}, P={self.chu_vi():.2f}"


# Không tạo được object từ class trừu tượng:
try:
    Hinh("gì đó")
except TypeError as e:
    print(f"   Hinh(...) → TypeError: {e}")

print("   ← đúng, vì Hinh chỉ là bản thiết kế, không phải hình cụ thể")


class HinhThieuMoi(Hinh):
    def dien_tich(self):
        return 0
    # cố tình quên chu_vi()


try:
    HinhThieuMoi("thiếu")
except TypeError as e:
    print(f"\n   lớp con thiếu method → TypeError:")
    print(f"     {e}")
    print("   ← lỗi ngay lúc TẠO object, và nói rõ thiếu method nào")


class HinhVuong(Hinh):
    def __init__(self, canh):
        super().__init__("Hình vuông")
        self.canh = canh

    def dien_tich(self):
        return self.canh ** 2

    def chu_vi(self):
        return 4 * self.canh


print(f"\n   lớp con đầy đủ: {HinhVuong(5).mo_ta()}")


# ---------------------------------------------------------------
# 3. ABSTRACT CLASS CÓ THỂ CHỨA CODE DÙNG CHUNG
# ---------------------------------------------------------------
print("\n3. CODE DÙNG CHUNG TRONG ABSTRACT CLASS")

# Đây là điểm khác biệt chính giữa abstract class và interface:
# abstract class CÓ THỂ chứa dữ liệu và code thật.


class TaiLieu(ABC):
    def __init__(self, tieu_de, ma):
        self.tieu_de = tieu_de
        self.ma = ma
        self.dang_cho_muon = False       # trạng thái dùng chung

    @abstractmethod
    def so_ngay_muon(self):
        """Mỗi loại tài liệu có hạn mượn khác nhau."""

    @abstractmethod
    def loai(self):
        """Tên loại, để in ra."""

    # --- phần CODE DÙNG CHUNG, viết một lần cho mọi loại ---
    def cho_muon(self):
        if self.dang_cho_muon:
            raise ValueError(f"{self.tieu_de} đang được mượn")
        self.dang_cho_muon = True
        return self.so_ngay_muon()

    def tra(self):
        if not self.dang_cho_muon:
            raise ValueError(f"{self.tieu_de} không ở trạng thái đang mượn")
        self.dang_cho_muon = False

    def phi_tre(self, so_ngay_tre):
        return max(0, so_ngay_tre) * 5_000

    def mo_ta(self):
        tt = "đang mượn" if self.dang_cho_muon else "có sẵn"
        return f"[{self.loai()}] {self.tieu_de} ({self.so_ngay_muon()} ngày) — {tt}"


class Sach(TaiLieu):
    def so_ngay_muon(self):
        return 30

    def loai(self):
        return "Sách"


class Bao(TaiLieu):
    def so_ngay_muon(self):
        return 3

    def loai(self):
        return "Báo"

    def phi_tre(self, so_ngay_tre):
        return max(0, so_ngay_tre) * 20_000      # báo trễ bị phạt nặng hơn


class DiaDVD(TaiLieu):
    def so_ngay_muon(self):
        return 7

    def loai(self):
        return "DVD"


kho = [Sach("Clean Code", "S01"), Bao("Tuổi Trẻ", "B01"), DiaDVD("Inception", "D01")]

for tl in kho:
    tl.cho_muon()
    print(f"   {tl.mo_ta()}")

print(f"\n   phí trễ 5 ngày:")
for tl in kho:
    print(f"     {tl.loai():5} {tl.phi_tre(5):>8,}")

print("""
   cho_muon(), tra(), mo_ta() viết MỘT LẦN trong lớp cha.
   Mỗi lớp con chỉ cần nói nó khác ở điểm nào (so_ngay_muon, loai, phi_tre).
   Đây là cách dùng abstract class đúng nhất.""")


# ---------------------------------------------------------------
# 4. TEMPLATE METHOD — một mẫu rất hay gặp
# ---------------------------------------------------------------
print("4. TEMPLATE METHOD")


class QuyTrinhXuLy(ABC):
    """Lớp cha định ra KHUNG, lớp con điền chi tiết."""

    def chay(self, nguon):
        """Khung cố định — lớp con không nên override method này."""
        du_lieu = self.doc(nguon)
        du_lieu = self.bien_doi(du_lieu)
        return self.ghi(du_lieu)

    @abstractmethod
    def doc(self, nguon): ...

    @abstractmethod
    def bien_doi(self, du_lieu): ...

    @abstractmethod
    def ghi(self, du_lieu): ...


class XuLyDiem(QuyTrinhXuLy):
    def doc(self, nguon):
        return [float(x) for x in nguon.split(",")]

    def bien_doi(self, du_lieu):
        return [min(10.0, d * 1.1) for d in du_lieu]      # cộng 10%, trần 10

    def ghi(self, du_lieu):
        return ", ".join(f"{d:.1f}" for d in du_lieu)


print(f"   vào:  7,8,9.5")
print(f"   ra:   {XuLyDiem().chay('7,8,9.5')}")
print("   ← thêm quy trình mới: chỉ cần cài 3 method, khung chay() không đổi")


# ---------------------------------------------------------------
# 5. @abstractmethod VỚI @property
# ---------------------------------------------------------------
print("\n5. ABSTRACT PROPERTY")


class XeCo(ABC):
    @property
    @abstractmethod                      # thứ tự quan trọng: property ở trên
    def so_banh(self):
        ...

    def mo_ta(self):
        return f"{type(self).__name__}: {self.so_banh} bánh"


class XeMay(XeCo):
    @property
    def so_banh(self):
        return 2


class XeTai(XeCo):
    @property
    def so_banh(self):
        return 6


for x in [XeMay(), XeTai()]:
    print(f"   {x.mo_ta()}")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_14_abstract.py
#
# 1. abstract class NhanVien với @abstractmethod luong().
#    Thêm method thường thue() = luong() * 0.1 dùng chung.
#    Tạo FullTime, PartTime, CongTacVien.
# 2. abstract class BoLoc với @abstractmethod kiem_tra(x), và method thường
#    ap_dung(danh_sach) dùng kiem_tra() — template method
# 3. Tạo một lớp con CỐ TÌNH thiếu một abstractmethod, chạy thử, đọc lỗi
# 4. abstract class KetNoi với @abstractmethod mo()/dong() và method thường
#    chay_lenh(sql) tự mở, chạy, rồi đóng (template method)
# 5. Tự trả lời: khi nào dùng abstract class, khi nào chỉ cần duck typing?
