"""
BÀI TẬP — 07-pythonic/17_dunder_methods.py
Chạy: python bt_17_dunder.py
"""


# --- BÀI 1 ------------------------------------------------------
class Tien:
    """__init__(so_tien, don_vi)
    __str__  -> "100.00 USD"
    __add__  -> cộng; raise ValueError nếu KHÁC đơn vị
    __eq__, __lt__ — chỉ so sánh được khi cùng đơn vị"""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class Vector2D:
    """__init__(x, y)
    __add__, __sub__   với Vector2D khác
    __mul__            nhân với một SỐ
    __abs__            độ dài = sqrt(x^2 + y^2)
    __eq__, __repr__   repr dạng "Vector2D(1, 2)" """
    # TODO


# --- BÀI 3 ------------------------------------------------------
class GioHang:
    """__init__(mon=None) — mon là list tuple (ten, gia)
    them(ten, gia)
    __len__, __iter__, __contains__ (theo TÊN món), __getitem__
    __add__ gộp hai giỏ thành giỏ MỚI
    tong() trả tổng giá"""
    # TODO


# --- BÀI 4 ------------------------------------------------------
class KhoangNgay:
    """__init__(bat_dau, ket_thuc) — hai số nguyên (số ngày từ mốc 0)
    __contains__  kiểm tra một ngày có trong khoảng (bao gồm hai đầu)
    __len__       số ngày trong khoảng (bao gồm hai đầu)
    __repr__      "KhoangNgay(1, 10)" """
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    a, b = Tien(100, "USD"), Tien(50, "USD")
    assert str(a) == "100.00 USD", f"bài 1: nhận {str(a)!r}"
    assert str(a + b) == "150.00 USD", "bài 1: cộng cùng đơn vị"
    assert a == Tien(100, "USD") and a != b, "bài 1: __eq__"
    assert b < a, "bài 1: __lt__"
    assert sorted([a, b])[0] == b, "bài 1: sorted dùng __lt__"
    try:
        a + Tien(50, "EUR")
        raise AssertionError("bài 1: phải chặn cộng khác đơn vị")
    except ValueError:
        pass

    v1, v2 = Vector2D(1, 2), Vector2D(3, 4)
    assert repr(v1) == "Vector2D(1, 2)", f"bài 2: nhận {repr(v1)!r}"
    assert v1 + v2 == Vector2D(4, 6), "bài 2: __add__"
    assert v2 - v1 == Vector2D(2, 2), "bài 2: __sub__"
    assert v1 * 3 == Vector2D(3, 6), "bài 2: __mul__ với số"
    assert abs(Vector2D(3, 4)) == 5.0, f"bài 2: nhận {abs(Vector2D(3, 4))}"

    g = GioHang()
    g.them("Táo", 30000)
    g.them("Cam", 25000)
    assert len(g) == 2, f"bài 3: nhận {len(g)}"
    assert "Táo" in g, "bài 3: __contains__ theo tên"
    assert "Xoài" not in g, "bài 3"
    assert g[0][0] == "Táo", "bài 3: __getitem__"
    assert [m[0] for m in g] == ["Táo", "Cam"], "bài 3: __iter__"
    assert g.tong() == 55000, f"bài 3: nhận {g.tong()}"

    g2 = GioHang()
    g2.them("Xoài", 40000)
    gop = g + g2
    assert len(gop) == 3 and gop.tong() == 95000, f"bài 3: gộp, nhận {gop.tong()}"
    assert len(g) == 2, "bài 3: __add__ không được sửa giỏ gốc"

    k = KhoangNgay(1, 10)
    assert repr(k) == "KhoangNgay(1, 10)", f"bài 4: nhận {repr(k)!r}"
    assert 5 in k and 1 in k and 10 in k, "bài 4: bao gồm hai đầu"
    assert 0 not in k and 11 not in k, "bài 4"
    assert len(k) == 10, f"bài 4: nhận {len(k)}"
    assert len(KhoangNgay(5, 5)) == 1, "bài 4: một ngày"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
