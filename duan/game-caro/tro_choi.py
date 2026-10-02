"""
Dự án 2 — điều phối trò chơi.

TroChoi CHỨA một BanCo và hai NguoiChoi (composition).
Nó không kế thừa gì — nhờ vậy đổi được bàn cờ, đổi được người chơi.

Chạy: python tro_choi.py
"""
from ban_co import BanCo


class TroChoi:
    def __init__(self, ban_co, nguoi_choi_1, nguoi_choi_2, im_lang=False):
        """im_lang=True thì không in gì — để chạy test và mô phỏng nhiều ván."""
        # TODO: lưu ban_co, danh sách 2 người chơi, chi_so_luot = 0, im_lang
        #       raise ValueError nếu hai người chơi dùng CÙNG một quân
        ...

    @property
    def nguoi_hien_tai(self):
        """Người đến lượt."""
        # TODO
        ...

    def doi_luot(self):
        # TODO
        ...

    def noi(self, *args):
        """In, trừ khi im_lang."""
        # TODO
        ...

    def choi_mot_luot(self):
        """Một lượt: hỏi người hiện tại chọn ô, đặt quân, đổi lượt.
        Trả về tuple (hang, cot) đã đi.

        Đây là chỗ ĐA HÌNH: gọi chon_o() mà không cần biết loại người chơi."""
        # TODO
        ...

    def ket_qua(self):
        """Trả về object NguoiChoi thắng, hoặc None nếu hòa / chưa xong."""
        # TODO
        ...

    def chay(self):
        """Lặp tới khi ban_co.ket_thuc(). In bàn cờ sau mỗi lượt (nếu không im_lang).
        Trả về người thắng hoặc None nếu hòa."""
        # TODO
        ...


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    from nguoi_choi import MayNgauNhien, MayThongMinh

    x = MayNgauNhien("Máy 1", "X", seed=1)
    o = MayNgauNhien("Máy 2", "O", seed=2)

    try:
        TroChoi(BanCo(), MayNgauNhien("A", "X"), MayNgauNhien("B", "X"))
        raise AssertionError("phải chặn hai người chơi cùng quân")
    except ValueError:
        pass

    g = TroChoi(BanCo(), x, o, im_lang=True)
    assert g.nguoi_hien_tai is x, "X đi trước"
    g.doi_luot()
    assert g.nguoi_hien_tai is o
    g.doi_luot()
    assert g.nguoi_hien_tai is x, "đổi lượt phải quay lại"

    o_da_di = g.choi_mot_luot()
    assert g.ban_co[o_da_di[0], o_da_di[1]] == "X", "phải đặt quân của người đi"
    assert g.nguoi_hien_tai is o, "đi xong phải đổi lượt"

    # chạy trọn ván — phải luôn kết thúc
    for seed in range(10):
        g = TroChoi(BanCo(),
                    MayNgauNhien("A", "X", seed=seed),
                    MayNgauNhien("B", "O", seed=seed + 100),
                    im_lang=True)
        thang = g.chay()
        assert g.ban_co.ket_thuc(), f"ván seed={seed} chưa kết thúc"
        if thang is None:
            assert g.ban_co.hoa(), "trả None thì phải là hòa"
        else:
            assert g.ban_co.nguoi_thang() == thang.quan, "người thắng phải khớp quân"

    # máy thông minh không được THUA máy ngẫu nhiên trên 3x3
    so_thua = 0
    for seed in range(30):
        g = TroChoi(BanCo(),
                    MayThongMinh("Thông minh", "X", seed=seed),
                    MayNgauNhien("Ngẫu nhiên", "O", seed=seed + 500),
                    im_lang=True)
        thang = g.chay()
        if thang is not None and thang.quan == "O":
            so_thua += 1
    assert so_thua == 0, \
        f"MayThongMinh thua {so_thua}/30 ván — kiểm tra lại logic chặn"

    # bàn 5x5 thắng 4 cũng phải chạy được, không sửa TroChoi
    g = TroChoi(BanCo(5, can_de_thang=4),
                MayThongMinh("A", "X", seed=1),
                MayNgauNhien("B", "O", seed=2),
                im_lang=True)
    g.chay()
    assert g.ban_co.ket_thuc(), "ván 5x5 phải kết thúc"

    print("tro_choi.py — ĐÚNG. Giờ chạy main.py để chơi thật")
