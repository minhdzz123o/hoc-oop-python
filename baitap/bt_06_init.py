"""
BÀI TẬP — 01-class-object/06_constructor_self.py
Chạy: python bt_06_init.py
"""


# --- BÀI 1 ------------------------------------------------------
class NgayThang:
    """__init__(ngay, thang, nam) — raise ValueError nếu
    thang ngoài 1-12 hoặc ngay ngoài 1-31.
    Thêm __str__ trả về "02/10/2026" (có số 0 đứng đầu)."""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class MatKhau:
    """__init__(chuoi) — raise ValueError nếu dưới 8 ký tự
    hoặc không chứa chữ số nào.
    Thêm method do_manh() trả về "yếu"/"vừa"/"mạnh":
      yếu  = chỉ có chữ và số
      vừa  = có thêm chữ hoa
      mạnh = có thêm ký tự đặc biệt (không phải chữ, không phải số)"""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class DanhSachViec:
    """__init__(ten, viec=None) — KHÔNG mắc bẫy mutable default.
    Method them(v), xong(v), con_lai() trả list việc chưa xong."""
    # TODO


# --- BÀI 4: trả lời bằng lời -----------------------------------
# Vì sao nên validate trong __init__ thay vì để người dùng tạo object
# rồi gán attribute sau?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    assert str(NgayThang(2, 10, 2026)) == "02/10/2026", \
        f"bài 1: nhận {str(NgayThang(2, 10, 2026))!r}"
    for ngay, thang in [(0, 5), (32, 5), (15, 0), (15, 13)]:
        try:
            NgayThang(ngay, thang, 2026)
            raise AssertionError(f"bài 1: phải chặn ngày {ngay} tháng {thang}")
        except ValueError:
            pass

    assert MatKhau("abcd1234").do_manh() == "yếu"
    assert MatKhau("Abcd1234").do_manh() == "vừa"
    assert MatKhau("Abcd1234!").do_manh() == "mạnh"
    for xau in ["abc123", "abcdefgh", "1234"]:
        try:
            MatKhau(xau)
            raise AssertionError(f"bài 2: phải chặn {xau!r}")
        except ValueError:
            pass

    d1 = DanhSachViec("Hôm nay")
    d2 = DanhSachViec("Mai")
    d1.them("mua sữa")
    d2.them("đi học")
    assert d1.con_lai() == ["mua sữa"], \
        f"bài 3: MẮC BẪY mutable default! nhận {d1.con_lai()}"
    assert d2.con_lai() == ["đi học"], f"bài 3: nhận {d2.con_lai()}"
    d1.them("gọi mẹ")
    d1.xong("mua sữa")
    assert d1.con_lai() == ["gọi mẹ"], f"bài 3: sau xong(), nhận {d1.con_lai()}"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
