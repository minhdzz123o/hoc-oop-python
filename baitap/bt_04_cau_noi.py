"""
BÀI TẬP — 00-nen-tang/04_dict_lam_doi_tuong.py

ĐỪNG viết class ở bài này. Mục đích là cảm nhận cái bất tiện trước,
để tuần 3 bạn hiểu class giải quyết vấn đề gì.

Chạy: python bt_04_cau_noi.py
"""


# --- BÀI 1: giỏ hàng bằng dict + hàm ----------------------------
def tao_gio(chu_hang):
    """Trả về dict {"chu_hang": ..., "mon": []}
    Mỗi món là dict {"ten":..., "gia":..., "sl":...}"""
    # TODO
    return {}


def them_mon(gio, ten, gia, sl=1):
    """Thêm món. Chặn gia <= 0 hoặc sl <= 0 bằng raise ValueError."""
    # TODO
    return gio


def tong_tien(gio):
    """Tổng gia * sl của mọi món."""
    # TODO
    return 0


# --- BÀI 2: chỉ ra cách phá -------------------------------------
# Viết code THỰC SỰ CHẠY ĐƯỢC làm hỏng giỏ hàng bằng cách gán trực tiếp,
# bỏ qua mọi kiểm tra trong them_mon().
def pha_cach_1(gio):
    """Ví dụ: gán số lượng âm vào một món đã có."""
    # TODO
    return gio


def pha_cach_2(gio):
    """Ví dụ: thêm một món không qua them_mon(), thiếu khóa, hoặc gõ sai khóa."""
    # TODO
    return gio


# --- BÀI 3: trả lời bằng lời -----------------------------------
# Nếu được "cấm" người ta chạm vào một khóa trong dict giỏ hàng,
# bạn sẽ cấm khóa nào? Vì sao?
#
# TRẢ LỜI:
# TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    g = tao_gio("Minh")
    assert g.get("chu_hang") == "Minh", "bài 1: thiếu khóa chu_hang"
    assert g.get("mon") == [], "bài 1: mon phải là list rỗng"

    them_mon(g, "Táo", 30000, 3)
    them_mon(g, "Cam", 25000)
    assert len(g["mon"]) == 2, f"bài 1: cần 2 món, nhận {len(g['mon'])}"
    assert tong_tien(g) == 115000, f"bài 1: cần 115000, nhận {tong_tien(g)}"

    for gia, sl in [(0, 1), (-5, 1), (1000, 0), (1000, -2)]:
        try:
            them_mon(g, "Xấu", gia, sl)
            raise AssertionError(f"bài 1: phải chặn gia={gia}, sl={sl}")
        except ValueError:
            pass

    g2 = tao_gio("Lan")
    them_mon(g2, "Táo", 10000, 1)
    truoc = tong_tien(g2)
    pha_cach_1(g2)
    assert tong_tien(g2) != truoc or g2["mon"][0]["sl"] < 0, \
        "bài 2: pha_cach_1 chưa thực sự làm hỏng gì"

    g3 = tao_gio("Hùng")
    pha_cach_2(g3)
    assert g3 != tao_gio("Hùng"), "bài 2: pha_cach_2 chưa thay đổi gì"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
    print("Giờ sang 01-class-object/05_class_object.py")
