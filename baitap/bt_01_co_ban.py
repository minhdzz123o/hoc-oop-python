"""
BÀI TẬP — 00-nen-tang/01_bien_dieu_kien_vonglap.py

Điền code vào chỗ TODO. Chạy lại tới khi thấy "TẤT CẢ BÀI TẬP ĐÚNG".
Lúc đầu file này SẼ BÁO LỖI — đó là bình thường.

Chạy: python bt_01_co_ban.py
"""


# --- BÀI 1: bảng cửu chương -------------------------------------
def bang_cuu_chuong(n):
    """Trả về list các chuỗi dạng "7 x 1 = 7" từ n x 1 đến n x 10."""
    # TODO
    return []


# --- BÀI 2: tổng số chia hết cho 3 ------------------------------
def tong_chia_het_3(den):
    """Tổng các số từ 1 đến den (bao gồm den) chia hết cho 3."""
    # TODO
    return 0


# --- BÀI 3: phân loại tuổi --------------------------------------
def phan_loai_tuoi(tuoi):
    """< 13 "Trẻ em" | 13-19 "Thiếu niên" | 20-59 "Người trưởng thành"
    | >= 60 "Người cao tuổi" """
    # TODO
    return ""


# --- BÀI 4: đếm chữ số -----------------------------------------
def dem_chu_so(n):
    """Số chữ số của n. Dùng while và // , KHÔNG dùng len(str(n)).
    dem_chu_so(0) phải trả về 1."""
    # TODO
    return 0


# ===============================================================
# TỰ KIỂM — đừng sửa phần dưới
# ===============================================================
if __name__ == "__main__":
    b = bang_cuu_chuong(7)
    assert len(b) == 10, f"bài 1: cần 10 dòng, nhận {len(b)}"
    assert b[0] == "7 x 1 = 7", f"bài 1: dòng đầu sai → {b[0]!r}"
    assert b[9] == "7 x 10 = 70", f"bài 1: dòng cuối sai → {b[9]!r}"

    assert tong_chia_het_3(10) == 18, f"bài 2: 3+6+9=18, nhận {tong_chia_het_3(10)}"
    assert tong_chia_het_3(100) == 1683, f"bài 2: nhận {tong_chia_het_3(100)}"
    assert tong_chia_het_3(2) == 0, "bài 2: không có số nào thì trả 0"

    for tuoi, mong in [(5, "Trẻ em"), (13, "Thiếu niên"), (19, "Thiếu niên"),
                       (20, "Người trưởng thành"), (59, "Người trưởng thành"),
                       (60, "Người cao tuổi"), (90, "Người cao tuổi")]:
        got = phan_loai_tuoi(tuoi)
        assert got == mong, f"bài 3: tuổi {tuoi} → cần {mong!r}, nhận {got!r}"

    for n, mong in [(1234567, 7), (0, 1), (9, 1), (10, 2), (999, 3)]:
        got = dem_chu_so(n)
        assert got == mong, f"bài 4: {n} có {mong} chữ số, nhận {got}"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
