"""
BÀI TẬP — 03-inheritance/11_override.py
Chạy: python bt_11_override.py
"""
import math


# --- BÀI 1 ------------------------------------------------------
class Hinh:
    """__init__(ten), dien_tich() trả 0"""
    # TODO


# Tạo HinhTron(r), HinhChuNhat(rong, cao), HinhTamGiac(day, cao)
# override dien_tich()
# TODO


def tong_dien_tich(cac_hinh):
    """Tổng diện tích của một list hình HỖN HỢP. Không dùng isinstance."""
    # TODO
    return 0.0


# --- BÀI 2 ------------------------------------------------------
class NguoiChoi:
    """__init__(ten), diem_thuong() trả 10"""
    # TODO


class NguoiChoiVIP:
    """Kế thừa, diem_thuong() = gấp đôi của cha. PHẢI dùng super()."""
    # TODO


class NguoiChoiMoi:
    """Kế thừa, diem_thuong() = của cha + 5. PHẢI dùng super()."""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class FileLog:
    """__init__(), ghi(msg) trả về chuỗi msg và lưu vào self.cac_dong"""
    # TODO


class FileLogCoThoiGian:
    """Kế thừa FileLog. ghi(msg) thêm tiền tố "[HH:MM] " vào đầu
    rồi gọi super().ghi(). Dùng tham số gio/phut để test được."""
    # TODO: __init__(self, gio=0, phut=0)


# --- BÀI 4: tự tạo ví dụ phá hợp đồng --------------------------
class ChaOnDinh:
    """xu_ly(x) — hợp đồng: nhận MỌI giá trị, luôn trả về chuỗi."""

    def xu_ly(self, x):
        return str(x)


class ConPhaHopDong:
    """Kế thừa ChaOnDinh, override xu_ly() THẮT CHẶT điều kiện
    (ví dụ chỉ nhận số) → phá hợp đồng."""
    # TODO


class ConDung:
    """Kế thừa ChaOnDinh, override xu_ly() mà KHÔNG phá hợp đồng
    (ví dụ: thêm tiền tố nhưng vẫn nhận mọi giá trị)."""
    # TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    hinh = [HinhTron(2), HinhChuNhat(3, 4), HinhTamGiac(6, 4)]
    assert abs(hinh[0].dien_tich() - math.pi * 4) < 1e-9
    assert hinh[1].dien_tich() == 12
    assert hinh[2].dien_tich() == 12
    mong = math.pi * 4 + 12 + 12
    assert abs(tong_dien_tich(hinh) - mong) < 1e-9, \
        f"bài 1: cần {mong:.4f}, nhận {tong_dien_tich(hinh):.4f}"
    assert tong_dien_tich([]) == 0, "bài 1: list rỗng → 0"

    assert NguoiChoi("A").diem_thuong() == 10
    assert NguoiChoiVIP("B").diem_thuong() == 20, "bài 2: VIP gấp đôi"
    assert NguoiChoiMoi("C").diem_thuong() == 15, "bài 2: người mới +5"

    f = FileLog()
    f.ghi("khởi động")
    assert f.cac_dong == ["khởi động"], f"bài 3: nhận {f.cac_dong}"

    ft = FileLogCoThoiGian(9, 30)
    ft.ghi("khởi động")
    assert ft.cac_dong == ["[09:30] khởi động"], f"bài 3: nhận {ft.cac_dong}"

    def dung_nhu_cha(obj):
        """Hàm viết cho ChaOnDinh — phải chạy với mọi lớp con đúng đắn."""
        return [obj.xu_ly(x) for x in [1, "a", None]]

    assert dung_nhu_cha(ChaOnDinh()) == ["1", "a", "None"]
    try:
        dung_nhu_cha(ConPhaHopDong())
        raise AssertionError("bài 4: ConPhaHopDong phải THỰC SỰ phá được hợp đồng")
    except AssertionError:
        raise
    except Exception:
        pass

    ket_qua = dung_nhu_cha(ConDung())
    assert len(ket_qua) == 3 and all(isinstance(r, str) for r in ket_qua), \
        "bài 4: ConDung phải không phá hợp đồng"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
