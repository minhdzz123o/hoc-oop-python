"""
BÀI TẬP — 05-abstraction/15_protocol_interface.py
Chạy: python bt_15_protocol.py
"""
from typing import Protocol, runtime_checkable


# --- BÀI 1 ------------------------------------------------------
class CoTheVe(Protocol):
    """Khai báo: cần có method ve() -> str"""
    # TODO


# Ba class KHÔNG kế thừa gì, chỉ khớp protocol:
class Nut:
    """__init__(nhan). ve() -> "[ OK ]" với nhãn OK"""
    # TODO


class BieuDo:
    """__init__(cac_gia_tri). ve() -> chuỗi cột bằng ký tự #,
    ví dụ [3,1] -> "###\n#" """
    # TODO


class BanDo:
    """__init__(rong, cao). ve() -> lưới ký tự . kích thước rong x cao"""
    # TODO


def render(cac_thu):
    """Trả về list chuỗi — kết quả ve() của từng thứ."""
    # TODO
    return []


# --- BÀI 2 ------------------------------------------------------
class LuuTru(Protocol):
    """lay(khoa) và dat(khoa, gia_tri)"""
    # TODO


class LuuTruRAM:
    # TODO
    pass


class LuuTruFile:
    """__init__(duong_dan) — lưu qua JSON"""
    # TODO


def sao_luu(nguon, dich, cac_khoa):
    """Copy giá trị các khóa từ nguon sang dich.
    Trả về số khóa đã copy (bỏ qua khóa không có)."""
    # TODO
    return 0


# --- BÀI 3 ------------------------------------------------------
@runtime_checkable
class CoTheSoSanh(Protocol):
    def diem(self) -> float:
        ...


class SanPham:
    """__init__(ten, danh_gia). diem() trả danh_gia"""
    # TODO


def loc_khop_protocol(cac_thu):
    """Từ một list HỖN HỢP, trả list các object khớp CoTheSoSanh.
    Dùng isinstance với protocol runtime_checkable."""
    # TODO
    return []


# --- BÀI 4: trả lời bằng lời -----------------------------------
# Cho class TaiLieu ở file 14 (dùng ABC): nếu bạn phải tích hợp một class
# tài liệu từ thư viện ngoài mà KHÔNG sửa được, bạn làm thế nào?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    import os
    import tempfile

    assert Nut("OK").ve() == "[ OK ]", f"bài 1: nhận {Nut('OK').ve()!r}"
    assert BieuDo([3, 1]).ve() == "###\n#", f"bài 1: nhận {BieuDo([3, 1]).ve()!r}"
    assert BanDo(3, 2).ve() == "...\n...", f"bài 1: nhận {BanDo(3, 2).ve()!r}"
    assert len(render([Nut("A"), BieuDo([2]), BanDo(2, 1)])) == 3
    for cls in (Nut, BieuDo, BanDo):
        assert cls.__bases__ == (object,), f"bài 1: {cls.__name__} không được kế thừa gì"

    a, b = LuuTruRAM(), LuuTruRAM()
    a.dat("x", 1)
    a.dat("y", 2)
    assert sao_luu(a, b, ["x", "y", "khong_co"]) == 2, "bài 2"
    assert b.lay("x") == 1 and b.lay("y") == 2, "bài 2: đã copy đúng"

    tmp = os.path.join(tempfile.gettempdir(), "bt15.json")
    if os.path.exists(tmp):
        os.remove(tmp)
    f = LuuTruFile(tmp)
    assert sao_luu(a, f, ["x"]) == 1, "bài 2: cùng hàm, đích khác loại"
    assert LuuTruFile(tmp).lay("x") == 1, "bài 2: đọc lại từ file"
    os.remove(tmp)

    hon_hop = [SanPham("A", 4.5), "chuỗi", 42, SanPham("B", 3.0), None]
    khop = loc_khop_protocol(hon_hop)
    assert len(khop) == 2, f"bài 3: cần 2 object khớp, nhận {len(khop)}"
    assert all(hasattr(x, "diem") for x in khop), "bài 3"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
