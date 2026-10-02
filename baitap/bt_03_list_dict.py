"""
BÀI TẬP — 00-nen-tang/03_list_dict.py
Chạy: python bt_03_list_dict.py
"""


# --- BÀI 1 ------------------------------------------------------
def chi_so_chan(ds):
    """Trả về list chỉ chứa số chẵn. Dùng list comprehension."""
    # TODO
    return []


# --- BÀI 2 ------------------------------------------------------
def dem_ky_tu(s):
    """Đếm số lần xuất hiện của mỗi ký tự, trả về dict.
    Bỏ qua dấu cách. Không phân biệt hoa/thường."""
    # TODO
    return {}


# --- BÀI 3: quản lý lớp bằng list[dict] -------------------------
def them_sv(lop, ten, diem):
    """Thêm {"ten": ..., "diem": ...} vào lop. Trả về lop."""
    # TODO
    return lop


def tim_sv(lop, ten):
    """Trả về dict của sinh viên, hoặc None nếu không có."""
    # TODO
    return None


def diem_cao_nhat(lop):
    """Trả về TÊN của sinh viên điểm cao nhất. Lớp rỗng → None."""
    # TODO
    return None


# --- BÀI 4 ------------------------------------------------------
def gop_dict(a, b):
    """Gộp hai dict. Khóa trùng thì lấy giá trị của b.
    Không được sửa a hay b."""
    # TODO
    return {}


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    assert chi_so_chan([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert chi_so_chan([1, 3, 5]) == [], "bài 1: không có số chẵn"
    assert chi_so_chan([]) == [], "bài 1: list rỗng"

    d = dem_ky_tu("Hello World")
    assert d.get("l") == 3, f"bài 2: 'l' xuất hiện 3 lần, nhận {d.get('l')}"
    assert d.get("o") == 2, f"bài 2: 'o' xuất hiện 2 lần, nhận {d.get('o')}"
    assert " " not in d, "bài 2: phải bỏ qua dấu cách"
    assert d.get("h") == 1, "bài 2: không phân biệt hoa/thường"

    lop = []
    them_sv(lop, "Minh", 8.5)
    them_sv(lop, "Lan", 9.2)
    them_sv(lop, "Hùng", 7.0)
    assert len(lop) == 3, f"bài 3: cần 3 sv, nhận {len(lop)}"
    assert lop[0]["ten"] == "Minh" and lop[0]["diem"] == 8.5

    assert tim_sv(lop, "Lan")["diem"] == 9.2, "bài 3: tim_sv tìm đúng"
    assert tim_sv(lop, "Không có") is None, "bài 3: không tìm thấy → None"
    assert diem_cao_nhat(lop) == "Lan", f"bài 3: nhận {diem_cao_nhat(lop)}"
    assert diem_cao_nhat([]) is None, "bài 3: lớp rỗng → None"

    a, b = {"x": 1, "y": 2}, {"y": 99, "z": 3}
    assert gop_dict(a, b) == {"x": 1, "y": 99, "z": 3}
    assert a == {"x": 1, "y": 2}, "bài 4: KHÔNG được sửa dict a"
    assert b == {"y": 99, "z": 3}, "bài 4: KHÔNG được sửa dict b"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
