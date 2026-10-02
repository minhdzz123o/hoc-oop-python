"""
BÀI TẬP — 07-pythonic/18_dataclass.py
Chạy: python bt_18_dataclass.py
"""
from dataclasses import dataclass, field, FrozenInstanceError


# --- BÀI 1: viết lại bằng @dataclass ---------------------------
# TODO: @dataclass class SinhVien: ten: str, diem: float, lop: str = "K20"
#       thêm method xep_loai() -> "Giỏi"/"Khá"/"Trung bình"/"Yếu"


# TODO: @dataclass class SanPham: ten: str, gia: float, so_luong: int = 1,
#       nhan: list[str] = field(default_factory=list)
#       thêm method tong()


# --- BÀI 2: frozen ---------------------------------------------
# TODO: @dataclass(frozen=True) class Tien: so_tien: float, don_vi: str = "VND"
#       method cong(khac) trả về Tien MỚI (không sửa tại chỗ),
#       raise ValueError nếu khác đơn vị


# --- BÀI 3: __post_init__ --------------------------------------
# TODO: @dataclass class KhoangNgay: bat_dau: int, ket_thuc: int
#       __post_init__ raise ValueError nếu ket_thuc < bat_dau
#       property so_ngay (chỉ đọc)


# --- BÀI 4: order=True ----------------------------------------
# TODO: @dataclass(order=True) class DiemThi: diem: float, ten: str
#       (thứ tự field quyết định cách sắp xếp — điểm trước, tên sau)


# --- BÀI 5: đếm dòng tiết kiệm được ---------------------------
# Lấy một class bạn viết ở tuần 3-4, chuyển sang @dataclass.
# Số dòng trước: TODO
# Số dòng sau:   TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    sv = SinhVien("Minh", 8.5)
    assert sv.lop == "K20", "bài 1: giá trị mặc định"
    assert "ten='Minh'" in repr(sv), f"bài 1: __repr__ tự sinh, nhận {repr(sv)}"
    assert sv == SinhVien("Minh", 8.5), "bài 1: __eq__ tự sinh"
    assert sv.xep_loai() == "Giỏi", f"bài 1: nhận {sv.xep_loai()}"
    assert SinhVien("A", 7.5).xep_loai() == "Khá"
    assert SinhVien("B", 5.5).xep_loai() == "Trung bình"
    assert SinhVien("C", 3.0).xep_loai() == "Yếu"

    s1, s2 = SanPham("Bàn", 100), SanPham("Ghế", 50, 4)
    s1.nhan.append("mới")
    assert s1.nhan == ["mới"] and s2.nhan == [], \
        f"bài 1: list phải độc lập (dùng field), nhận {s1.nhan} / {s2.nhan}"
    assert s2.tong() == 200, f"bài 1: nhận {s2.tong()}"

    t = Tien(100, "USD")
    assert t.cong(Tien(50, "USD")) == Tien(150, "USD"), "bài 2"
    assert t == Tien(100, "USD"), "bài 2: bản gốc không đổi"
    assert bool({t: "x"}), "bài 2: frozen thì hashable"
    try:
        t.so_tien = 0
        raise AssertionError("bài 2: frozen phải chặn gán")
    except FrozenInstanceError:
        pass
    try:
        t.cong(Tien(50, "EUR"))
        raise AssertionError("bài 2: phải chặn cộng khác đơn vị")
    except ValueError:
        pass

    k = KhoangNgay(1, 10)
    assert k.so_ngay == 10, f"bài 3: nhận {k.so_ngay}"
    try:
        KhoangNgay(10, 1)
        raise AssertionError("bài 3: phải chặn ket_thuc < bat_dau")
    except ValueError:
        pass

    ds = [DiemThi(8.5, "Minh"), DiemThi(9.2, "Lan"), DiemThi(7.0, "Hùng")]
    assert sorted(ds)[0].ten == "Hùng", "bài 4: sắp theo điểm tăng dần"
    assert max(ds).ten == "Lan", "bài 4"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
