"""
Dự án 2 — bàn cờ.

Chạy: python ban_co.py
"""


class BanCo:
    TRONG = "."

    def __init__(self, kich_thuoc=3, can_de_thang=None):
        """can_de_thang mặc định = kich_thuoc (3x3 thắng 3, 5x5 thắng 5).
        Truyền riêng để làm được bàn 5x5 thắng 4."""
        # TODO: lưu kich_thuoc, can_de_thang,
        #       và _o là list 2 chiều toàn TRONG
        #       (nhớ bẫy ở file 05: đừng để các hàng dùng chung một list!)
        ...

    # --- đọc ---

    def __getitem__(self, vi_tri):
        """ban_co[1, 2] trả về quân ở hàng 1 cột 2."""
        # TODO
        ...

    def __str__(self):
        """In bàn cờ có số hàng/cột. Với 3x3:

              0 1 2
           0 . . .
           1 . X .
           2 . . O
        """
        # TODO
        ...

    def trong_ban(self, hang, cot):
        """True nếu toạ độ nằm trong bàn."""
        # TODO
        ...

    def o_trong(self):
        """List các tuple (hang, cot) còn trống."""
        # TODO
        ...

    def day(self):
        """True nếu không còn ô trống."""
        # TODO
        ...

    # --- ghi ---

    def dat(self, hang, cot, quan):
        """Đặt quân. raise ValueError nếu ngoài bàn hoặc ô đã có quân."""
        # TODO
        ...

    def xoa(self, hang, cot):
        """Trả ô về trống. Cần cho MayThongMinh khi thử nước đi."""
        # TODO
        ...

    # --- luật thắng ---

    def nguoi_thang(self):
        """Trả "X", "O" hoặc None.
        Kiểm tra mọi hàng, cột, và hai hướng chéo, tìm chuỗi
        can_de_thang quân giống nhau liên tiếp.

        Gợi ý: với mỗi ô có quân, thử 4 hướng (phải, xuống,
        chéo xuống-phải, chéo xuống-trái) và đếm xem đi được bao xa."""
        # TODO
        ...

    def hoa(self):
        """Hết ô mà chưa ai thắng."""
        # TODO
        ...

    def ket_thuc(self):
        """Có người thắng HOẶC hòa."""
        # TODO
        ...


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    b = BanCo()
    assert b[0, 0] == BanCo.TRONG, "ô mới phải trống"
    assert len(b.o_trong()) == 9, f"3x3 có 9 ô, nhận {len(b.o_trong())}"
    assert b.day() is False and b.ket_thuc() is False

    b.dat(1, 1, "X")
    assert b[1, 1] == "X"
    assert len(b.o_trong()) == 8

    # mỗi hàng phải là list RIÊNG (bẫy ở file 05)
    assert b[0, 1] == BanCo.TRONG, "đặt ở hàng 1 không được ảnh hưởng hàng 0"

    try:
        b.dat(1, 1, "O")
        raise AssertionError("phải chặn ô đã có quân")
    except ValueError:
        pass
    for hang, cot in [(-1, 0), (0, 3), (3, 3)]:
        try:
            b.dat(hang, cot, "O")
            raise AssertionError(f"phải chặn toạ độ ({hang},{cot})")
        except ValueError:
            pass

    b.xoa(1, 1)
    assert b[1, 1] == BanCo.TRONG, "xoa() phải trả ô về trống"

    ve = str(BanCo())
    assert "0 1 2" in ve.replace("  ", " "), f"__str__ thiếu số cột:\n{ve}"

    # thắng theo hàng
    b1 = BanCo()
    for cot in range(3):
        b1.dat(0, cot, "X")
    assert b1.nguoi_thang() == "X", "thắng theo hàng ngang"

    # thắng theo cột
    b2 = BanCo()
    for hang in range(3):
        b2.dat(hang, 2, "O")
    assert b2.nguoi_thang() == "O", "thắng theo cột"

    # thắng chéo xuống-phải
    b3 = BanCo()
    for i in range(3):
        b3.dat(i, i, "X")
    assert b3.nguoi_thang() == "X", "thắng chéo chính"

    # thắng chéo xuống-trái
    b4 = BanCo()
    for i in range(3):
        b4.dat(i, 2 - i, "O")
    assert b4.nguoi_thang() == "O", "thắng chéo phụ"

    # chưa ai thắng
    b5 = BanCo()
    b5.dat(0, 0, "X")
    b5.dat(1, 1, "O")
    assert b5.nguoi_thang() is None, "chưa ai thắng"

    # hòa: X O X / X O O / O X X
    b6 = BanCo()
    the_tran = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    for h in range(3):
        for c in range(3):
            b6.dat(h, c, the_tran[h][c])
    assert b6.nguoi_thang() is None, f"thế trận này không ai thắng:\n{b6}"
    assert b6.hoa() is True and b6.ket_thuc() is True, "phải là hòa"

    # bàn 5x5 thắng 4
    b7 = BanCo(5, can_de_thang=4)
    for cot in range(4):
        b7.dat(2, cot, "X")
    assert b7.nguoi_thang() == "X", "5x5 thắng 4 quân"

    b8 = BanCo(5, can_de_thang=4)
    for cot in range(3):
        b8.dat(2, cot, "X")
    assert b8.nguoi_thang() is None, "3 quân chưa đủ thắng khi cần 4"

    print("ban_co.py — ĐÚNG. Sang nguoi_choi.py")
