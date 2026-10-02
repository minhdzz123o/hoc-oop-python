"""
BÀI TẬP — 02-encapsulation/09_property.py
Chạy: python bt_09_property.py
"""


# --- BÀI 1 ------------------------------------------------------
class HinhVuong:
    """__init__(canh)
    property canh  — setter raise ValueError nếu <= 0
    property dien_tich, chu_vi — CHỈ ĐỌC (không có setter)"""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class NguoiDung:
    """__init__(email)
    property email — setter raise ValueError nếu không có "@" và "."
                     và chuẩn hóa về chữ thường
    property ten_mien — CHỈ ĐỌC, trả phần sau dấu @"""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class KhoangThoiGian:
    """__init__(giay) — bên trong CHỈ lưu MỘT giá trị
    property giay, phut, gio — đọc và ghi được cả ba
    setter chặn giá trị âm"""
    # TODO


# --- BÀI 4 ------------------------------------------------------
class SanPham:
    """__init__(gia, giam_gia=0.0)
    property giam_gia — setter chặn ngoài khoảng 0..1
    property gia_cuoi — CHỈ ĐỌC = gia * (1 - giam_gia)"""
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    h = HinhVuong(5)
    assert h.dien_tich == 25, f"bài 1: nhận {h.dien_tich}"
    assert h.chu_vi == 20, f"bài 1: nhận {h.chu_vi}"
    h.canh = 3
    assert h.dien_tich == 9, "bài 1: đổi cạnh thì diện tích đổi theo"
    for xau in [0, -5]:
        try:
            h.canh = xau
            raise AssertionError(f"bài 1: phải chặn cạnh {xau}")
        except ValueError:
            pass
    try:
        h.dien_tich = 100
        raise AssertionError("bài 1: dien_tich phải CHỈ ĐỌC")
    except AttributeError:
        pass

    u = NguoiDung("MINH@Example.COM")
    assert u.email == "minh@example.com", f"bài 2: nhận {u.email!r}"
    assert u.ten_mien == "example.com", f"bài 2: nhận {u.ten_mien!r}"
    for xau in ["khongco", "thieu@daucham", "khongcoa.com"]:
        try:
            u.email = xau
            raise AssertionError(f"bài 2: phải chặn {xau!r}")
        except ValueError:
            pass

    k = KhoangThoiGian(3660)
    assert k.giay == 3660, f"bài 3: nhận {k.giay}"
    assert k.phut == 61, f"bài 3: 3660 giây = 61 phút, nhận {k.phut}"
    assert abs(k.gio - 1.0166666666666666) < 1e-9, f"bài 3: nhận {k.gio}"
    k.phut = 120
    assert k.giay == 7200, f"bài 3: gán 120 phút → 7200 giây, nhận {k.giay}"
    k.gio = 2
    assert k.giay == 7200, f"bài 3: gán 2 giờ → 7200 giây, nhận {k.giay}"
    assert len([v for v in vars(k).values()]) == 1, \
        "bài 3: bên trong chỉ được lưu MỘT giá trị"
    try:
        k.giay = -1
        raise AssertionError("bài 3: phải chặn số âm")
    except ValueError:
        pass

    s = SanPham(100000, 0.2)
    assert s.gia_cuoi == 80000, f"bài 4: nhận {s.gia_cuoi}"
    s.giam_gia = 0.5
    assert s.gia_cuoi == 50000, f"bài 4: nhận {s.gia_cuoi}"
    for xau in [-0.1, 1.5]:
        try:
            s.giam_gia = xau
            raise AssertionError(f"bài 4: phải chặn giảm giá {xau}")
        except ValueError:
            pass

    print("TẤT CẢ BÀI TẬP ĐÚNG")
