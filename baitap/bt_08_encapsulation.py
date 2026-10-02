"""
BÀI TẬP — 02-encapsulation/08_private_getter_setter.py
Chạy: python bt_08_encapsulation.py
"""


# --- BÀI 1 ------------------------------------------------------
class TheHocSinh:
    """__init__(ten) — bên trong giữ _diem là dict {mon: diem}
    them_diem(mon, diem)  raise ValueError nếu diem ngoài 0-10
    diem_tb()             trung bình các môn, chưa có môn nào thì trả 0
    xem_diem()            trả BẢN COPY của dict (sửa bản đó không ảnh hưởng)"""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class MatKhauLuuTru:
    """__init__(mat_khau) — KHÔNG có cách nào đọc lại mật khẩu.
    kiem_tra(chuoi) trả True/False.
    Không được có method/attribute nào trả về mật khẩu gốc."""
    # TODO


# --- BÀI 3: ba cách phá class không đóng gói --------------------
class TaiKhoanHo:
    """Bản KHÔNG đóng gói — cho sẵn, đừng sửa."""

    def __init__(self, chu, so_du=0):
        self.chu = chu
        self.so_du = so_du
        self.lich_su = []

    def rut(self, tien):
        if tien > self.so_du:
            raise ValueError("Không đủ số dư")
        self.so_du -= tien
        self.lich_su.append(f"rút {tien}")


def pha_1(tk):
    """Làm số dư thành số âm."""
    # TODO
    return tk


def pha_2(tk):
    """Làm lịch sử sai lệch so với số dư thực tế."""
    # TODO
    return tk


def pha_3(tk):
    """Đổi chủ tài khoản, hoặc gán số dư thành kiểu không phải số."""
    # TODO
    return tk


# --- BÀI 4: trả lời bằng lời -----------------------------------
# Nếu Python không thực sự chặn được _attribute, thì dấu _ có ích gì?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    t = TheHocSinh("Minh")
    assert t.diem_tb() == 0, "bài 1: chưa có môn nào → 0"
    t.them_diem("Toán", 9)
    t.them_diem("Lý", 8)
    assert t.diem_tb() == 8.5, f"bài 1: nhận {t.diem_tb()}"
    for diem in [-1, 11, 100]:
        try:
            t.them_diem("Xấu", diem)
            raise AssertionError(f"bài 1: phải chặn điểm {diem}")
        except ValueError:
            pass
    ban_copy = t.xem_diem()
    ban_copy["Hóa"] = 0
    assert "Hóa" not in t.xem_diem(), "bài 1: xem_diem() phải trả BẢN COPY"

    m = MatKhauLuuTru("bimat123")
    assert m.kiem_tra("bimat123") is True, "bài 2: mật khẩu đúng"
    assert m.kiem_tra("sai") is False, "bài 2: mật khẩu sai"
    lo = [v for v in vars(m).values() if v == "bimat123"]
    assert not lo, "bài 2: mật khẩu gốc bị lưu nguyên văn — hãy lưu dạng hash"

    tk = TaiKhoanHo("Minh", 1000)
    pha_1(tk)
    assert tk.so_du < 0, "bài 3: pha_1 chưa làm số dư âm"

    tk2 = TaiKhoanHo("Lan", 1000)
    pha_2(tk2)
    assert tk2.so_du != 1000 or tk2.lich_su, "bài 3: pha_2 chưa gây sai lệch"

    tk3 = TaiKhoanHo("Hùng", 1000)
    pha_3(tk3)
    assert tk3.chu != "Hùng" or not isinstance(tk3.so_du, (int, float)), \
        "bài 3: pha_3 chưa phá được gì"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
