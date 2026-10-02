"""
BÀI TẬP — 07-pythonic/19_classmethod_staticmethod.py
Chạy: python bt_19_classmethod.py
"""


# --- BÀI 1 ------------------------------------------------------
class NhietDo:
    """__init__(celsius=0.0), property celsius/fahrenheit/kelvin
    @classmethod tu_fahrenheit(f), tu_kelvin(k)"""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class SinhVien:
    """__init__(ten, diem, lop)
    @classmethod tu_dong_csv("Minh,8.5,K20")
    @classmethod tu_dict({"ten":..., "diem":..., "lop":...})
    __eq__ để so sánh được trong test"""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class CauHinh:
    """__init__(host, port, debug=False)
    @classmethod mac_dinh() -> host="localhost", port=8000, debug=False
    @classmethod tu_file(duong_dan) -> đọc JSON
    __eq__"""
    # TODO


# --- BÀI 4 ------------------------------------------------------
class ThoiLuong:
    """__init__(giay)
    @classmethod tu_phut(p), tu_gio(g), tu_chuoi("1:30:00")
    @staticmethod hop_le(chuoi) -> True nếu đúng dạng H:MM:SS
    __str__ -> "1:30:00"
    __eq__"""
    # TODO


# --- BÀI 5: trả lời bằng lời -----------------------------------
# Tìm trong code bạn đã viết: có class nào CHỈ GỒM staticmethod không?
# Nếu có, nó nên là gì thay vì class?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    import json
    import os
    import tempfile

    n = NhietDo.tu_fahrenheit(212)
    assert abs(n.celsius - 100) < 1e-9, f"bài 1: nhận {n.celsius}"
    n2 = NhietDo.tu_kelvin(273.15)
    assert abs(n2.celsius) < 1e-9, f"bài 1: nhận {n2.celsius}"
    assert abs(NhietDo(25).fahrenheit - 77) < 1e-9, "bài 1"

    sv = SinhVien.tu_dong_csv("Minh,8.5,K20")
    assert sv.ten == "Minh" and sv.diem == 8.5 and sv.lop == "K20", \
        f"bài 2: nhận {sv.ten}, {sv.diem}, {sv.lop}"
    assert sv == SinhVien.tu_dict({"ten": "Minh", "diem": 8.5, "lop": "K20"}), \
        "bài 2: hai cách tạo phải cho object bằng nhau"

    c = CauHinh.mac_dinh()
    assert c.host == "localhost" and c.port == 8000 and c.debug is False, "bài 3"

    tmp = os.path.join(tempfile.gettempdir(), "bt19_cfg.json")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"host": "1.2.3.4", "port": 9000, "debug": True}, f)
    c2 = CauHinh.tu_file(tmp)
    assert c2.host == "1.2.3.4" and c2.port == 9000 and c2.debug is True, "bài 3"
    os.remove(tmp)

    assert ThoiLuong.tu_phut(90) == ThoiLuong(5400), "bài 4: tu_phut"
    assert ThoiLuong.tu_gio(2) == ThoiLuong(7200), "bài 4: tu_gio"
    assert ThoiLuong.tu_chuoi("1:30:00") == ThoiLuong(5400), "bài 4: tu_chuoi"
    assert str(ThoiLuong(5400)) == "1:30:00", f"bài 4: nhận {str(ThoiLuong(5400))!r}"
    assert str(ThoiLuong(45)) == "0:00:45", f"bài 4: nhận {str(ThoiLuong(45))!r}"

    assert ThoiLuong.hop_le("1:30:00") is True, "bài 4: hop_le đúng dạng"
    for xau in ["abc", "1:30", "1:70:00", ""]:
        assert ThoiLuong.hop_le(xau) is False, f"bài 4: {xau!r} phải không hợp lệ"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
    print()
    print("Bạn đã xong toàn bộ bài tập. Giờ làm dự án trong duan/")
