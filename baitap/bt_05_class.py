"""
BÀI TẬP — 01-class-object/05_class_object.py
Chạy: python bt_05_class.py
"""


# --- BÀI 1 ------------------------------------------------------
class HinhChuNhat:
    """__init__(rong, cao), method dien_tich(), chu_vi(), la_hinh_vuong()"""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class Sach:
    """__init__(tieu_de, tac_gia, so_trang)
    method mo_ta() trả về: "Clean Code — Robert Martin (464 trang)" """
    # TODO


# --- BÀI 3 ------------------------------------------------------
class BoDem:
    """Đếm từ 0. Method tang(), giam(), reset(), xem().
    giam() không cho xuống dưới 0."""
    # TODO


# --- BÀI 4: chứng minh bẫy class attribute ----------------------
class ChuoiSoSai:
    """CỐ TÌNH khai list ở thân class để thấy bug."""
    # TODO: khai `cac_so = []` ở thân class, thêm method them(x)


class ChuoiSoDung:
    """Khai list trong __init__ — đúng."""
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    h = HinhChuNhat(3, 4)
    assert h.dien_tich() == 12, f"bài 1: diện tích, nhận {h.dien_tich()}"
    assert h.chu_vi() == 14, f"bài 1: chu vi, nhận {h.chu_vi()}"
    assert h.la_hinh_vuong() is False, "bài 1: 3x4 không phải hình vuông"
    assert HinhChuNhat(5, 5).la_hinh_vuong() is True, "bài 1: 5x5 là hình vuông"

    s = Sach("Clean Code", "Robert Martin", 464)
    assert s.mo_ta() == "Clean Code — Robert Martin (464 trang)", \
        f"bài 2: nhận {s.mo_ta()!r}"

    b = BoDem()
    assert b.xem() == 0, "bài 3: bắt đầu từ 0"
    b.tang(); b.tang(); b.tang()
    assert b.xem() == 3, f"bài 3: sau 3 lần tang, nhận {b.xem()}"
    b.giam()
    assert b.xem() == 2, f"bài 3: sau giam, nhận {b.xem()}"
    b.reset()
    assert b.xem() == 0, "bài 3: reset về 0"
    b.giam()
    assert b.xem() == 0, "bài 3: giam không được xuống dưới 0"

    b2 = BoDem()
    b2.tang()
    assert b.xem() == 0 and b2.xem() == 1, "bài 3: hai bộ đếm phải độc lập"

    a1, a2 = ChuoiSoSai(), ChuoiSoSai()
    a1.them(1); a2.them(2)
    assert a1.cac_so == [1, 2], \
        f"bài 4: phải thấy BUG dùng chung list, nhận {a1.cac_so}"

    d1, d2 = ChuoiSoDung(), ChuoiSoDung()
    d1.them(1); d2.them(2)
    assert d1.cac_so == [1] and d2.cac_so == [2], \
        f"bài 4: bản đúng phải độc lập, nhận {d1.cac_so} / {d2.cac_so}"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
