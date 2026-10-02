"""
BÀI TẬP — 04-polymorphism/12_da_hinh.py
Chạy: python bt_12_da_hinh.py
"""


# --- BÀI 1 ------------------------------------------------------
class PhuongTien:
    """__init__(ten), toc_do() trả 0,
    thoi_gian_di(km) = km / toc_do()  (giờ)"""
    # TODO


# Tạo XeDap (15km/h), XeMay (40), OTo (60),
# MayBay (800 nhưng thoi_gian_di CỘNG THÊM 2 giờ làm thủ tục)
# TODO


def nhanh_nhat(cac_pt, km):
    """Trả về object phương tiện nhanh nhất cho khoảng cách km.
    KHÔNG dùng isinstance."""
    # TODO
    return None


# --- BÀI 2 ------------------------------------------------------
class BoLoc:
    """kiem_tra(x) trả True/False.
    ap_dung(ds) trả list các phần tử thỏa kiem_tra()."""
    # TODO


class LocSoChan:
    # TODO
    pass


class LocSoNguyenTo:
    # TODO
    pass


class LocLonHon:
    """__init__(n) — giữ lại phần tử > n"""
    # TODO


def ap_dung_nhieu(ds, cac_bo_loc):
    """Áp dụng lần lượt từng bộ lọc lên kết quả của bộ trước."""
    # TODO
    return []


# --- BÀI 3 ------------------------------------------------------
class ThanhToan:
    """xu_ly(so_tien) trả về số tiền THỰC SỰ bị trừ (gồm phí)"""
    # TODO


class TheTinDung:
    """phí 2%"""
    # TODO


class ViDienTu:
    """phí 0.5%"""
    # TODO


class ChuyenKhoan:
    """phí cố định 5000"""
    # TODO


# --- BÀI 4: so sánh với if/elif --------------------------------
def thoi_gian_di_kieu_if(loai, km):
    """Viết lại bài 1 bằng chuỗi if/elif trên chuỗi `loai`
    ("xedap", "xemay", "oto", "maybay")."""
    # TODO
    return 0.0


# Thêm một loại phương tiện mới (ví dụ tàu hỏa 120km/h):
#   - cách đa hình phải sửa bao nhiêu chỗ?  TODO
#   - cách if/elif phải sửa bao nhiêu chỗ?  TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    pt = [XeDap("xe đạp"), XeMay("xe máy"), OTo("ô tô"), MayBay("máy bay")]
    assert pt[0].thoi_gian_di(30) == 2.0, f"bài 1: nhận {pt[0].thoi_gian_di(30)}"
    assert pt[1].thoi_gian_di(80) == 2.0
    assert abs(pt[3].thoi_gian_di(800) - 3.0) < 1e-9, \
        f"bài 1: máy bay 800km = 1h bay + 2h thủ tục, nhận {pt[3].thoi_gian_di(800)}"
    assert nhanh_nhat(pt, 20).ten == "ô tô", \
        f"bài 1: 20km thì ô tô nhanh nhất, nhận {nhanh_nhat(pt, 20).ten}"
    assert nhanh_nhat(pt, 2000).ten == "máy bay", "bài 1: 2000km thì máy bay"

    ds = list(range(1, 21))
    assert LocSoChan().ap_dung(ds) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert LocSoNguyenTo().ap_dung(ds) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert LocLonHon(15).ap_dung(ds) == [16, 17, 18, 19, 20]
    assert ap_dung_nhieu(ds, [LocSoChan(), LocLonHon(10)]) == [12, 14, 16, 18, 20]

    assert TheTinDung().xu_ly(1_000_000) == 1_020_000
    assert ViDienTu().xu_ly(1_000_000) == 1_005_000
    assert ChuyenKhoan().xu_ly(1_000_000) == 1_005_000

    assert thoi_gian_di_kieu_if("xedap", 30) == 2.0, "bài 4"
    assert abs(thoi_gian_di_kieu_if("maybay", 800) - 3.0) < 1e-9, "bài 4"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
