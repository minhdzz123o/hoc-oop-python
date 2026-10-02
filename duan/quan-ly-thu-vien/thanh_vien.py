"""
Dự án 1 — thành viên thư viện.

Chạy: python thanh_vien.py
"""


class ThanhVien:
    """Lớp cha. _dang_muon được ĐÓNG GÓI — chỉ đổi qua method."""

    TOI_DA = 3

    def __init__(self, ma, ten):
        # TODO: lưu ma, ten, và _dang_muon = [] (list các TaiLieu)
        ...

    @property
    def dang_muon(self):
        """Trả về BẢN COPY — không cho sửa list nội bộ từ ngoài."""
        # TODO
        ...

    @property
    def toi_da(self):
        """Lấy từ TOI_DA của class THẬT SỰ (dùng type(self), không viết cứng)."""
        # TODO
        ...

    def con_cho_muon(self):
        """Còn mượn được bao nhiêu nữa."""
        # TODO
        ...

    def nhan(self, tai_lieu):
        """Thêm tài liệu vào danh sách đang mượn.
        raise ValueError nếu đã đạt hạn mức."""
        # TODO
        ...

    def tra_lai(self, tai_lieu):
        """Bỏ tài liệu khỏi danh sách.
        raise ValueError nếu thành viên không mượn cái đó."""
        # TODO
        ...

    def he_so_phi(self):
        """Nhân vào phí trễ. Thành viên thường = 1.0"""
        # TODO
        ...

    def mo_ta(self):
        """Ví dụ: "TV01 Minh (thường) — 2/3 tài liệu" """
        # TODO
        ...

    def loai(self):
        """Tên loại thành viên, để in ra."""
        return "thường"

    def __repr__(self):
        return f"{type(self).__name__}({self.ma!r}, {self.ten!r})"


class ThanhVienThuong(ThanhVien):
    """Tối đa 3, phí trễ bình thường."""
    # TODO


class ThanhVienVIP(ThanhVien):
    """Tối đa 10, KHÔNG chịu phí trễ (he_so_phi = 0)."""
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    from tai_lieu import Sach, DiaDVD

    tv = ThanhVienThuong("TV01", "Minh")
    vip = ThanhVienVIP("TV02", "Lan")

    assert tv.toi_da == 3, f"thường tối đa 3, nhận {tv.toi_da}"
    assert vip.toi_da == 10, f"VIP tối đa 10, nhận {vip.toi_da}"
    assert tv.con_cho_muon() == 3 and vip.con_cho_muon() == 10

    assert tv.he_so_phi() == 1.0, "thường chịu phí đầy đủ"
    assert vip.he_so_phi() == 0, "VIP không chịu phí trễ"

    s1, s2, s3, s4 = (Sach(f"S0{i}", f"Sách {i}") for i in range(1, 5))

    tv.nhan(s1)
    tv.nhan(s2)
    assert len(tv.dang_muon) == 2, f"nhận {len(tv.dang_muon)}"
    assert tv.con_cho_muon() == 1

    ban_copy = tv.dang_muon
    ban_copy.append(s3)
    assert len(tv.dang_muon) == 2, "dang_muon phải trả BẢN COPY"

    tv.nhan(s3)
    try:
        tv.nhan(s4)
        raise AssertionError("phải chặn khi quá hạn mức 3")
    except ValueError:
        pass

    tv.tra_lai(s1)
    assert len(tv.dang_muon) == 2, "sau khi trả còn 2"
    try:
        tv.tra_lai(s1)
        raise AssertionError("phải chặn trả cái không mượn")
    except ValueError:
        pass

    for i in range(10):
        vip.nhan(DiaDVD(f"D{i:02d}", f"Phim {i}"))
    assert vip.con_cho_muon() == 0
    try:
        vip.nhan(Sach("S99", "Thêm"))
        raise AssertionError("VIP cũng có hạn mức 10")
    except ValueError:
        pass

    mo_ta = tv.mo_ta()
    for phan in ["TV01", "Minh", "thường", "2", "3"]:
        assert phan in mo_ta, f"mo_ta() thiếu {phan!r}: {mo_ta!r}"
    assert "VIP" in vip.mo_ta(), f"mo_ta() của VIP: {vip.mo_ta()!r}"

    print("thanh_vien.py — ĐÚNG. Sang thu_vien.py")
