"""
BÀI TẬP — 04-polymorphism/13_duck_typing.py
Chạy: python bt_13_duck_typing.py
"""
import json
import os
import tempfile


# --- BÀI 1: ba class KHÔNG kế thừa nhau -------------------------
class GhiFile:
    """__init__(duong_dan). ghi(dong) ghi thêm một dòng vào file."""
    # TODO


class GhiManHinh:
    """ghi(dong) in ra màn hình. Giữ self.so_dong để test được."""
    # TODO


class GhiBoNho:
    """ghi(dong) thêm vào self.cac_dong."""
    # TODO


def ghi_log(bo_ghi, cac_dong):
    """Dùng được với CẢ BA class trên. Không isinstance, không kế thừa."""
    # TODO
    return None


# --- BÀI 2: cái giả để test ------------------------------------
class LuuTruFile:
    """__init__(duong_dan). lay(khoa) / dat(khoa, gia_tri) qua file JSON."""
    # TODO


class LuuTruGia:
    """Cùng method lay/dat nhưng chỉ dùng dict trong RAM."""
    # TODO


def dem_truy_cap(luu_tru, cac_khoa):
    """Gọi lay() cho từng khóa, trả về số khóa CÓ giá trị (không None)."""
    # TODO
    return 0


# --- BÀI 3 ------------------------------------------------------
def tong_an_toan(cac_thu):
    """Cộng mọi phần tử cộng được, BỎ QUA phần tử không cộng được.
    PHẢI dùng try/except, KHÔNG dùng isinstance."""
    # TODO
    return 0


# --- BÀI 4: trả lời bằng lời -----------------------------------
# Duck typing có ưu điểm gì so với interface của Java, và nhược điểm gì?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    bn = GhiBoNho()
    ghi_log(bn, ["a", "b", "c"])
    assert bn.cac_dong == ["a", "b", "c"], f"bài 1: nhận {bn.cac_dong}"

    mh = GhiManHinh()
    ghi_log(mh, ["x", "y"])
    assert mh.so_dong == 2, f"bài 1: nhận {mh.so_dong}"

    tmp = os.path.join(tempfile.gettempdir(), "bt13_log.txt")
    if os.path.exists(tmp):
        os.remove(tmp)
    ghi_log(GhiFile(tmp), ["dòng 1", "dòng 2"])
    with open(tmp, encoding="utf-8") as f:
        assert len(f.read().strip().split("\n")) == 2, "bài 1: file phải có 2 dòng"
    os.remove(tmp)

    assert not hasattr(GhiBoNho, "__bases__") or GhiBoNho.__bases__ == (object,), \
        "bài 1: ba class KHÔNG được kế thừa nhau"

    gia = LuuTruGia()
    gia.dat("a", 1)
    gia.dat("b", 2)
    assert gia.lay("a") == 1 and gia.lay("khong_co") is None
    assert dem_truy_cap(gia, ["a", "b", "khong_co"]) == 2, \
        f"bài 2: nhận {dem_truy_cap(gia, ['a', 'b', 'khong_co'])}"

    tmp2 = os.path.join(tempfile.gettempdir(), "bt13_store.json")
    if os.path.exists(tmp2):
        os.remove(tmp2)
    lf = LuuTruFile(tmp2)
    lf.dat("x", 10)
    assert LuuTruFile(tmp2).lay("x") == 10, "bài 2: phải đọc lại được từ file"
    os.remove(tmp2)

    assert tong_an_toan([1, 2, 3]) == 6
    assert tong_an_toan([1, "a", 2, None, 3.5]) == 6.5, \
        f"bài 3: nhận {tong_an_toan([1, 'a', 2, None, 3.5])}"
    assert tong_an_toan([]) == 0
    assert tong_an_toan(["a", "b"]) == 0, "bài 3: không có gì cộng được → 0"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
