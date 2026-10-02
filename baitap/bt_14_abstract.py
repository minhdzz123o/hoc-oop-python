"""
BÀI TẬP — 05-abstraction/14_abstract_class.py
Chạy: python bt_14_abstract.py
"""
from abc import ABC, abstractmethod


# --- BÀI 1 ------------------------------------------------------
class NhanVien(ABC):
    """__init__(ten)
    @abstractmethod luong()
    method thường thue() = luong() * 0.1  — dùng chung cho mọi lớp con"""
    # TODO


class FullTime:
    """Kế thừa NhanVien. __init__(ten, luong_thang)"""
    # TODO


class PartTime:
    """Kế thừa NhanVien. __init__(ten, luong_gio, so_gio)"""
    # TODO


class CongTacVien:
    """Kế thừa NhanVien. __init__(ten, phi_du_an) — không chịu thuế (thue()=0)"""
    # TODO


# --- BÀI 2: template method ------------------------------------
class BoLoc(ABC):
    """@abstractmethod kiem_tra(x)
    method thường ap_dung(ds) dùng kiem_tra() — viết MỘT LẦN"""
    # TODO


class LocChan:
    # TODO
    pass


class LocDaiHon:
    """__init__(n) — giữ chuỗi dài hơn n ký tự"""
    # TODO


# --- BÀI 3: lớp con thiếu abstractmethod -----------------------
class ThieuMethod:
    """Kế thừa NhanVien nhưng CỐ TÌNH không cài luong().
    Chạy thử, đọc lỗi, ghi lại vào comment.
    LỖI NHẬN ĐƯỢC: TODO"""
    # TODO


# --- BÀI 4: template method cho kết nối ------------------------
class KetNoi(ABC):
    """@abstractmethod mo() và dong()
    method thường chay_lenh(sql): tự mo(), chạy, rồi dong().
    Trả về list các bước đã làm, ví dụ ["mở", "chạy: SELECT 1", "đóng"]"""
    # TODO


class KetNoiGia:
    """Kế thừa KetNoi, mo()/dong() chỉ ghi lại vào self.nhat_ky"""
    # TODO


# --- BÀI 5: trả lời bằng lời -----------------------------------
# Khi nào dùng abstract class, khi nào chỉ cần duck typing?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    try:
        NhanVien("X")
        raise AssertionError("bài 1: NhanVien phải là abstract, không tạo được")
    except TypeError:
        pass

    ft = FullTime("Minh", 15_000_000)
    pt = PartTime("Lan", 80_000, 100)
    ctv = CongTacVien("Hùng", 5_000_000)

    assert ft.luong() == 15_000_000
    assert pt.luong() == 8_000_000
    assert ctv.luong() == 5_000_000
    assert ft.thue() == 1_500_000, f"bài 1: nhận {ft.thue()}"
    assert pt.thue() == 800_000, "bài 1: thue() dùng chung từ lớp cha"
    assert ctv.thue() == 0, "bài 1: CTV không chịu thuế"

    assert LocChan().ap_dung([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert LocDaiHon(3).ap_dung(["a", "abcd", "ab", "abcde"]) == ["abcd", "abcde"]

    try:
        ThieuMethod("X")
        raise AssertionError("bài 3: phải không tạo được vì thiếu luong()")
    except TypeError:
        pass

    kn = KetNoiGia()
    buoc = kn.chay_lenh("SELECT 1")
    assert buoc == ["mở", "chạy: SELECT 1", "đóng"], f"bài 4: nhận {buoc}"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
