"""
Dự án 1 — class điều phối. Phần khó nhất.

ThuVien CHỨA tài liệu và thành viên (composition), không kế thừa gì.

Chạy: python thu_vien.py
"""
import json

from tai_lieu import Sach, Bao, DiaDVD
from thanh_vien import ThanhVienThuong, ThanhVienVIP

# Dùng để tạo lại object đúng loại khi đọc từ JSON
LOAI_TAI_LIEU = {"Sach": Sach, "Bao": Bao, "DiaDVD": DiaDVD}
LOAI_THANH_VIEN = {"ThanhVienThuong": ThanhVienThuong, "ThanhVienVIP": ThanhVienVIP}


class ThuVien:
    def __init__(self, ten):
        # TODO: lưu ten, _kho = [] (list TaiLieu), _thanh_vien = [] (list ThanhVien)
        ...

    # --- thêm vào thư viện ---

    def them_tai_lieu(self, tl):
        """raise ValueError nếu đã có tài liệu cùng mã."""
        # TODO
        ...

    def them_thanh_vien(self, tv):
        """raise ValueError nếu đã có thành viên cùng mã."""
        # TODO
        ...

    # --- tra cứu ---

    def tim_tai_lieu(self, ma):
        """Trả về TaiLieu hoặc None."""
        # TODO
        ...

    def tim_thanh_vien(self, ma):
        """Trả về ThanhVien hoặc None."""
        # TODO
        ...

    def co_san(self):
        """List tài liệu chưa ai mượn."""
        # TODO
        ...

    # --- nghiệp vụ chính ---

    def cho_muon(self, ma_tv, ma_tl):
        """Kiểm tra theo thứ tự rồi mới thay đổi gì:
          1. thành viên tồn tại           → ValueError nếu không
          2. tài liệu tồn tại             → ValueError nếu không
          3. tài liệu chưa ai mượn        → ValueError nếu đang mượn
          4. thành viên còn hạn mức       → ValueError nếu hết
        Rồi gọi tai_lieu.cho_muon() và thanh_vien.nhan().
        Trả về chuỗi: "Minh mượn [Clean Code] trong 30 ngày"

        LƯU Ý: nếu bước nào thất bại thì KHÔNG được để lại trạng thái
        nửa vời (ví dụ tài liệu đã đánh dấu mượn nhưng thành viên chưa nhận).
        """
        # TODO
        ...

    def tra(self, ma_tv, ma_tl, so_ngay_tre=0):
        """Trả tài liệu. Trả về SỐ TIỀN phí phải đóng.
        Phí = tai_lieu.phi_tre(so_ngay_tre) * thanh_vien.he_so_phi()
        raise ValueError nếu thành viên không mượn tài liệu đó."""
        # TODO
        ...

    # --- báo cáo ---

    def bao_cao(self):
        """Chuỗi nhiều dòng gồm:
          - tên thư viện
          - số tài liệu theo từng loại (dùng loai() — đây là ĐA HÌNH)
          - số đang được mượn / tổng
          - từng thành viên đang mượn gì
        Tự do về định dạng, miễn có đủ thông tin."""
        # TODO
        ...

    # --- lưu / tải ---

    def luu(self, duong_dan):
        """Ghi JSON. Gợi ý cấu trúc:
        {
          "ten": ...,
          "kho": [{"loai": "Sach", "ma":..., "tieu_de":..., "tac_gia":...,
                   "dang_cho_muon": false}, ...],
          "thanh_vien": [{"loai": "ThanhVienVIP", "ma":..., "ten":...,
                          "dang_muon": ["S01", ...]}, ...]
        }
        Lưu MÃ tài liệu trong dang_muon, không lưu cả object."""
        # TODO
        ...

    @classmethod
    def tai(cls, duong_dan):
        """Đọc JSON, tạo lại ThuVien đầy đủ.
        Dùng LOAI_TAI_LIEU / LOAI_THANH_VIEN để tạo đúng class.
        Nhớ khôi phục cả trạng thái đang mượn."""
        # TODO
        ...

    def __len__(self):
        """Tổng số tài liệu."""
        # TODO
        ...

    def __repr__(self):
        return f"ThuVien({self.ten!r}, {len(self)} tài liệu)"


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    import os
    import tempfile

    tv = ThuVien("Thư viện Quốc gia")
    tv.them_tai_lieu(Sach("S01", "Clean Code", "Robert Martin"))
    tv.them_tai_lieu(Sach("S02", "Refactoring", "Martin Fowler"))
    tv.them_tai_lieu(Bao("B01", "Tuổi Trẻ"))
    tv.them_tai_lieu(DiaDVD("D01", "Inception"))
    tv.them_thanh_vien(ThanhVienThuong("TV01", "Minh"))
    tv.them_thanh_vien(ThanhVienVIP("TV02", "Lan"))

    assert len(tv) == 4, f"nhận {len(tv)}"
    assert len(tv.co_san()) == 4, "ban đầu tất cả có sẵn"

    try:
        tv.them_tai_lieu(Sach("S01", "Trùng mã"))
        raise AssertionError("phải chặn mã trùng")
    except ValueError:
        pass

    assert tv.tim_tai_lieu("S01").tieu_de == "Clean Code"
    assert tv.tim_tai_lieu("KHONG_CO") is None
    assert tv.tim_thanh_vien("TV01").ten == "Minh"

    kq = tv.cho_muon("TV01", "S01")
    assert "Minh" in kq and "Clean Code" in kq and "30" in kq, f"nhận {kq!r}"
    assert len(tv.co_san()) == 3, "sau khi mượn còn 3 có sẵn"

    try:
        tv.cho_muon("TV02", "S01")
        raise AssertionError("phải chặn mượn cái đang có người mượn")
    except ValueError:
        pass
    try:
        tv.cho_muon("KHONG_CO", "S02")
        raise AssertionError("phải chặn thành viên không tồn tại")
    except ValueError:
        pass
    try:
        tv.cho_muon("TV01", "KHONG_CO")
        raise AssertionError("phải chặn tài liệu không tồn tại")
    except ValueError:
        pass

    # hạn mức: Minh (thường) tối đa 3
    tv.cho_muon("TV01", "S02")
    tv.cho_muon("TV01", "B01")
    try:
        tv.cho_muon("TV01", "D01")
        raise AssertionError("phải chặn khi Minh đã mượn 3")
    except ValueError:
        pass
    # và không được để lại trạng thái nửa vời
    assert tv.tim_tai_lieu("D01").dang_cho_muon is False, \
        "lần mượn thất bại không được đánh dấu tài liệu là đang mượn"

    # phí: sách trễ 5 ngày = 25,000; Minh là thường nên hệ số 1.0
    phi = tv.tra("TV01", "S01", so_ngay_tre=5)
    assert phi == 25_000, f"phí trễ, nhận {phi}"
    assert len(tv.co_san()) == 2, "sau khi trả"

    # VIP không chịu phí
    tv.cho_muon("TV02", "S01")
    assert tv.tra("TV02", "S01", so_ngay_tre=10) == 0, "VIP miễn phí trễ"

    try:
        tv.tra("TV02", "D01")
        raise AssertionError("phải chặn trả cái không mượn")
    except ValueError:
        pass

    bc = tv.bao_cao()
    for phan in ["Thư viện Quốc gia", "Sách", "Báo", "DVD", "Minh"]:
        assert phan in bc, f"bao_cao() thiếu {phan!r}"

    tmp = os.path.join(tempfile.gettempdir(), "thuvien_test.json")
    tv.luu(tmp)
    tv2 = ThuVien.tai(tmp)
    assert tv2.ten == tv.ten and len(tv2) == len(tv), "tải lại phải giống bản gốc"
    assert len(tv2.co_san()) == len(tv.co_san()), "trạng thái đang mượn phải khôi phục"
    assert type(tv2.tim_tai_lieu("B01")).__name__ == "Bao", "phải tạo lại ĐÚNG loại"
    assert tv2.tim_thanh_vien("TV02").toi_da == 10, "VIP phải được tạo lại đúng loại"
    assert len(tv2.tim_thanh_vien("TV01").dang_muon) == 2, "khôi phục danh sách mượn"
    os.remove(tmp)

    print("thu_vien.py — ĐÚNG. Sang main.py")
