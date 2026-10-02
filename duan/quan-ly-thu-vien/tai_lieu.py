"""
Dự án 1 — tài liệu trong thư viện.

Chạy: python tai_lieu.py   (tự kiểm phần này trước khi sang file sau)
"""
from abc import ABC, abstractmethod


class TaiLieu(ABC):
    """Abstract class: định ra khung chung cho mọi loại tài liệu.

    Lớp con PHẢI cài: so_ngay_muon(), loai()
    Lớp con DÙNG CHUNG: cho_muon(), tra(), phi_tre(), mo_ta()
    """

    PHI_TRE_MOI_NGAY = 5_000

    def __init__(self, ma, tieu_de, tac_gia=""):
        # TODO: lưu ma, tieu_de, tac_gia
        #       và _dang_cho_muon = False (đóng gói: chỉ đổi qua method)
        ...

    # --- lớp con phải cài đặt ---

    @abstractmethod
    def so_ngay_muon(self):
        """Số ngày được mượn tối đa."""

    @abstractmethod
    def loai(self):
        """Tên loại, ví dụ "Sách"."""

    # --- dùng chung cho mọi loại ---

    @property
    def dang_cho_muon(self):
        """Chỉ đọc — không cho gán trực tiếp từ bên ngoài."""
        # TODO
        ...

    def cho_muon(self):
        """Đánh dấu đang mượn, trả về số ngày được mượn.
        raise ValueError nếu đang có người mượn."""
        # TODO
        ...

    def tra(self):
        """Đánh dấu đã trả. raise ValueError nếu nó không đang được mượn."""
        # TODO
        ...

    def phi_tre(self, so_ngay_tre):
        """PHI_TRE_MOI_NGAY * số ngày trễ. Trễ âm hoặc 0 thì không phí."""
        # TODO
        ...

    def mo_ta(self):
        """Ví dụ: "[Sách] S01 — Clean Code (Robert Martin), 30 ngày, có sẵn" """
        # TODO
        ...

    def __repr__(self):
        return f"{type(self).__name__}({self.ma!r}, {self.tieu_de!r})"


class Sach(TaiLieu):
    """30 ngày."""
    # TODO


class Bao(TaiLieu):
    """3 ngày. Phí trễ GẤP 4 lần bình thường — override phi_tre()."""
    # TODO


class DiaDVD(TaiLieu):
    """7 ngày."""
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    try:
        TaiLieu("X", "Y")
        raise AssertionError("TaiLieu phải là abstract, không tạo được object")
    except TypeError:
        pass

    s = Sach("S01", "Clean Code", "Robert Martin")
    b = Bao("B01", "Tuổi Trẻ")
    d = DiaDVD("D01", "Inception")

    assert s.so_ngay_muon() == 30 and b.so_ngay_muon() == 3 and d.so_ngay_muon() == 7
    assert (s.loai(), b.loai(), d.loai()) == ("Sách", "Báo", "DVD")

    assert s.dang_cho_muon is False, "mới tạo thì có sẵn"
    assert s.cho_muon() == 30, "cho_muon() trả số ngày"
    assert s.dang_cho_muon is True
    try:
        s.cho_muon()
        raise AssertionError("phải chặn mượn cái đang được mượn")
    except ValueError:
        pass
    s.tra()
    assert s.dang_cho_muon is False
    try:
        s.tra()
        raise AssertionError("phải chặn trả cái không ai mượn")
    except ValueError:
        pass

    try:
        s.dang_cho_muon = True
        raise AssertionError("dang_cho_muon phải CHỈ ĐỌC (property không setter)")
    except AttributeError:
        pass

    assert s.phi_tre(5) == 25_000, f"sách trễ 5 ngày, nhận {s.phi_tre(5)}"
    assert b.phi_tre(5) == 100_000, f"báo trễ gấp 4, nhận {b.phi_tre(5)}"
    assert s.phi_tre(0) == 0 and s.phi_tre(-3) == 0, "không trễ thì không phí"

    mo_ta = s.mo_ta()
    for phan in ["Sách", "S01", "Clean Code", "Robert Martin", "30"]:
        assert phan in mo_ta, f"mo_ta() thiếu {phan!r}: {mo_ta!r}"

    print("tai_lieu.py — ĐÚNG. Sang thanh_vien.py")
