"""
Dự án 2 — người chơi.

Đây là chỗ ĐA HÌNH thể hiện rõ nhất: TroChoi gọi chon_o() mà không cần
biết đó là người thật hay máy loại nào.

Chạy: python nguoi_choi.py
"""
import random
from abc import ABC, abstractmethod

from ban_co import BanCo


class NguoiChoi(ABC):
    def __init__(self, ten, quan):
        # TODO: lưu ten và quan ("X" hoặc "O")
        ...

    @abstractmethod
    def chon_o(self, ban_co):
        """Trả về tuple (hang, cot) — PHẢI là ô còn trống."""

    def quan_doi_thu(self):
        """"X" nếu mình là "O", và ngược lại."""
        # TODO
        ...

    def __str__(self):
        return f"{self.ten} ({self.quan})"


class NguoiChoiNguoi(NguoiChoi):
    """Đọc từ bàn phím. Nhập sai thì hỏi lại, không crash.

    Để test được, __init__ nhận thêm nguon_nhap: một hàm trả về chuỗi.
    Mặc định là input(), khi test thì truyền hàm giả."""

    def __init__(self, ten, quan, nguon_nhap=input):
        # TODO
        ...

    def chon_o(self, ban_co):
        """Hỏi tới khi nhận được toạ độ hợp lệ.
        Chấp nhận các dạng: "1 2" hoặc "1,2".
        Nhập sai định dạng / ngoài bàn / ô đã có quân → in lời nhắc, hỏi lại."""
        # TODO
        ...


class MayNgauNhien(NguoiChoi):
    """Chọn một ô trống bất kỳ."""

    def __init__(self, ten, quan, seed=None):
        # TODO: lưu một random.Random(seed) riêng để test lặp lại được
        ...

    def chon_o(self, ban_co):
        # TODO
        ...


class MayThongMinh(NguoiChoi):
    """Thứ tự ưu tiên:
      1. nước thắng ngay của MÌNH
      2. chặn nước thắng ngay của ĐỐI THỦ
      3. ô trung tâm (nếu bàn có tâm và tâm còn trống)
      4. một góc còn trống
      5. ngẫu nhiên

    Gợi ý cho bước 1 và 2: thử đặt quân vào từng ô trống, gọi
    ban_co.nguoi_thang(), rồi ban_co.xoa() để trả lại nguyên trạng.
    """

    def __init__(self, ten, quan, seed=None):
        # TODO
        ...

    def _o_thang_cho(self, ban_co, quan):
        """Trả ô đầu tiên mà đặt `quan` vào là thắng ngay, hoặc None.
        PHẢI trả bàn cờ về nguyên trạng sau khi thử."""
        # TODO
        ...

    def _tam(self, ban_co):
        """Toạ độ ô giữa nếu kích thước lẻ, ngược lại None."""
        # TODO
        ...

    def _cac_goc(self, ban_co):
        """4 góc của bàn."""
        # TODO
        ...

    def chon_o(self, ban_co):
        # TODO
        ...


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    try:
        NguoiChoi("X", "X")
        raise AssertionError("NguoiChoi phải là abstract")
    except TypeError:
        pass

    nc = MayNgauNhien("Máy", "X", seed=1)
    assert nc.quan == "X" and nc.quan_doi_thu() == "O"
    assert MayNgauNhien("M", "O").quan_doi_thu() == "X"
    assert str(nc) == "Máy (X)", f"nhận {str(nc)!r}"

    # ngẫu nhiên: luôn chọn ô TRỐNG
    for _ in range(20):
        b = BanCo()
        b.dat(0, 0, "X")
        b.dat(1, 1, "O")
        o = MayNgauNhien("M", "X").chon_o(b)
        assert o in b.o_trong(), f"chọn ô không trống: {o}"

    # cùng seed thì cùng kết quả
    b = BanCo()
    a1 = MayNgauNhien("M", "X", seed=42).chon_o(b)
    a2 = MayNgauNhien("M", "X", seed=42).chon_o(b)
    assert a1 == a2, "cùng seed phải cho cùng nước đi"

    may = MayThongMinh("Máy", "X", seed=1)

    # 1. thắng ngay được thì phải thắng
    b = BanCo()
    b.dat(0, 0, "X")
    b.dat(0, 1, "X")
    b.dat(1, 0, "O")
    assert may.chon_o(b) == (0, 2), f"phải thắng ngay ở (0,2), chọn {may.chon_o(b)}"
    assert b[0, 2] == BanCo.TRONG, "thử nước đi xong phải trả bàn về nguyên trạng"

    # 2. chặn đối thủ
    b = BanCo()
    b.dat(2, 0, "O")
    b.dat(2, 1, "O")
    b.dat(0, 0, "X")
    assert may.chon_o(b) == (2, 2), f"phải chặn ở (2,2), chọn {may.chon_o(b)}"

    # thắng ưu tiên hơn chặn
    b = BanCo()
    b.dat(0, 0, "X")
    b.dat(0, 1, "X")      # X thắng được ở (0,2)
    b.dat(2, 0, "O")
    b.dat(2, 1, "O")      # O cũng thắng được ở (2,2)
    assert may.chon_o(b) == (0, 2), "thắng phải ưu tiên hơn chặn"

    # 3. chiếm tâm
    b = BanCo()
    b.dat(0, 0, "O")
    assert may.chon_o(b) == (1, 1), f"phải chiếm tâm, chọn {may.chon_o(b)}"

    # 4. tâm đã bị chiếm thì lấy góc
    b = BanCo()
    b.dat(1, 1, "O")
    assert may.chon_o(b) in [(0, 0), (0, 2), (2, 0), (2, 2)], "phải lấy góc"

    # người chơi: nhập sai rồi nhập đúng
    cac_lan_nhap = iter(["abc", "9 9", "1 1", "0 0"])
    nguoi = NguoiChoiNguoi("Minh", "X", nguon_nhap=lambda *a: next(cac_lan_nhap))
    b = BanCo()
    b.dat(1, 1, "O")      # (1,1) đã có quân → phải hỏi lại
    assert nguoi.chon_o(b) == (0, 0), "phải bỏ qua mọi lần nhập sai"

    cac_lan_nhap2 = iter(["2,0"])
    nguoi2 = NguoiChoiNguoi("Lan", "O", nguon_nhap=lambda *a: next(cac_lan_nhap2))
    assert nguoi2.chon_o(BanCo()) == (2, 0), "phải chấp nhận dạng 'h,c'"

    print("nguoi_choi.py — ĐÚNG. Sang tro_choi.py")
