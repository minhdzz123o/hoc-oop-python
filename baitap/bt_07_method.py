"""
BÀI TẬP — 01-class-object/07_method_vs_function.py
Chạy: python bt_07_method.py
"""


# --- BÀI 1 ------------------------------------------------------
class MayTinhBoTui:
    """Giữ một giá trị hiện tại (bắt đầu 0).
    cong(x), tru(x), nhan(x), chia(x) — mỗi cái PHẢI return self
    để gọi chuỗi được: mt.cong(5).nhan(3)
    xoa() đặt lại về 0, ket_qua() trả giá trị hiện tại.
    chia(0) raise ZeroDivisionError."""
    # TODO


# --- BÀI 2 ------------------------------------------------------
class ChuoiVanBan:
    """__init__(noi_dung)
    dem_tu()          số từ (tách theo dấu cách)
    dem_ky_tu()       số ký tự KHÔNG tính dấu cách
    viet_hoa_dau_cau() trả chuỗi mới, viết hoa chữ đầu mỗi câu
                       (câu kết thúc bằng . ! ?)"""
    # TODO


# --- BÀI 3 ------------------------------------------------------
class ThoiKhoaBieu:
    """them_tiet(thu, mon)  thu là 2..7
    xem_thu(thu)           trả list môn của thứ đó (rỗng nếu chưa có)
    tong_tiet()            tổng số tiết cả tuần"""
    # TODO


# --- BÀI 4: trả lời bằng lời -----------------------------------
# Trong 3 class trên, method nào là TRUY VẤN (chỉ đọc),
# method nào là HÀNH ĐỘNG (thay đổi trạng thái)?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    mt = MayTinhBoTui()
    assert mt.ket_qua() == 0, "bài 1: bắt đầu từ 0"
    assert mt.cong(5).nhan(3).ket_qua() == 15, \
        f"bài 1: gọi chuỗi phải được 15, nhận {mt.ket_qua()}"
    mt.xoa()
    assert mt.ket_qua() == 0, "bài 1: xoa() về 0"
    assert mt.cong(10).tru(3).chia(7).ket_qua() == 1, f"bài 1: nhận {mt.ket_qua()}"
    try:
        MayTinhBoTui().cong(5).chia(0)
        raise AssertionError("bài 1: chia(0) phải raise ZeroDivisionError")
    except ZeroDivisionError:
        pass

    c = ChuoiVanBan("hello world. xin chao! ban khoe khong?")
    assert c.dem_tu() == 7, f"bài 2: cần 7 từ, nhận {c.dem_tu()}"
    assert c.dem_ky_tu() == 32, f"bài 2: nhận {c.dem_ky_tu()}"
    assert c.viet_hoa_dau_cau() == "Hello world. Xin chao! Ban khoe khong?", \
        f"bài 2: nhận {c.viet_hoa_dau_cau()!r}"

    tkb = ThoiKhoaBieu()
    tkb.them_tiet(2, "Toán")
    tkb.them_tiet(2, "Lý")
    tkb.them_tiet(4, "Hóa")
    assert tkb.xem_thu(2) == ["Toán", "Lý"], f"bài 3: nhận {tkb.xem_thu(2)}"
    assert tkb.xem_thu(6) == [], "bài 3: thứ chưa có tiết → list rỗng"
    assert tkb.tong_tiet() == 3, f"bài 3: nhận {tkb.tong_tiet()}"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
