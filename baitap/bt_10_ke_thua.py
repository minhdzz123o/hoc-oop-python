"""
BÀI TẬP — 03-inheritance/10_ke_thua_super.py
Chạy: python bt_10_ke_thua.py
"""


# --- BÀI 1 ------------------------------------------------------
class DongVat:
    """__init__(ten), method keu() và di_chuyen()"""
    # TODO


# Tạo Cho, Meo, Chim, Ca kế thừa DongVat:
#   Cho.keu()  -> "Woof",  Cho.di_chuyen()  -> "chạy"
#   Meo.keu()  -> "Meow",  Meo.di_chuyen()  -> "chạy"
#   Chim.keu() -> "Tweet", Chim.di_chuyen() -> "bay"
#   Ca.keu()   -> "...",   Ca.di_chuyen()   -> "bơi"
# TODO


# --- BÀI 2 ------------------------------------------------------
class TaiKhoan:
    """__init__(chu, so_du=0), rut(tien) chặn quá số dư, nap(tien)"""
    # TODO


class TaiKhoanTietKiem:
    """Kế thừa TaiKhoan. __init__ thêm lai_suat.
    tinh_lai() trả về so_du * lai_suat (không cộng vào số dư)."""
    # TODO


class TaiKhoanThanhToan:
    """Kế thừa TaiKhoan. __init__ thêm phi_giao_dich.
    rut(tien) trừ thêm phí — dùng super().rut()."""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class Xe:
    """__init__(bien_so), phi_cau_duong() trả 0"""
    # TODO


class XeMay:
    """Kế thừa Xe, phi_cau_duong() -> 10000"""
    # TODO


class XeTai:
    """Kế thừa Xe. __init__ thêm tan_trong.
    phi_cau_duong() -> 50000 + tan_trong * 20000"""
    # TODO


# --- BÀI 4: cố tình quên super().__init__() --------------------
class ConQuenSuper:
    """Kế thừa DongVat nhưng CỐ TÌNH không gọi super().__init__().
    Chạy thử, đọc lỗi, rồi viết lỗi đó vào comment dưới đây.
    LỖI NHẬN ĐƯỢC: TODO"""
    # TODO


# --- BÀI 5: trả lời bằng lời -----------------------------------
# Trong 3 bài trên, có chỗ nào đáng lẽ nên dùng composition không?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    vuon = [Cho("Mực"), Meo("Miu"), Chim("Sẻ"), Ca("Vàng")]
    assert [a.keu() for a in vuon] == ["Woof", "Meow", "Tweet", "..."]
    assert [a.di_chuyen() for a in vuon] == ["chạy", "chạy", "bay", "bơi"]
    assert all(isinstance(a, DongVat) for a in vuon), "bài 1: phải kế thừa DongVat"
    assert vuon[0].ten == "Mực", "bài 1: __init__ của cha phải được gọi"

    tk = TaiKhoanTietKiem("Minh", 1_000_000, 0.06)
    assert tk.tinh_lai() == 60_000, f"bài 2: nhận {tk.tinh_lai()}"
    assert isinstance(tk, TaiKhoan), "bài 2: phải kế thừa TaiKhoan"

    tt = TaiKhoanThanhToan("Lan", 100_000, 5_000)
    tt.rut(50_000)
    assert tt.so_du == 45_000, f"bài 2: rút 50k + phí 5k, nhận {tt.so_du}"
    try:
        tt.rut(45_000)
        raise AssertionError("bài 2: phải chặn vì 45k + 5k phí > 45k số dư")
    except ValueError:
        pass

    assert XeMay("29X1-123").phi_cau_duong() == 10_000
    assert XeTai("29C-456", 5).phi_cau_duong() == 150_000, \
        f"bài 3: nhận {XeTai('29C-456', 5).phi_cau_duong()}"

    try:
        ConQuenSuper("Test").keu()
        print("  (bài 4: class của bạn không lỗi — đã gọi super()? hãy bỏ nó đi)")
    except AttributeError:
        pass

    print("TẤT CẢ BÀI TẬP ĐÚNG")
