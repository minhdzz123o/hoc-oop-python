"""
Dự án 2 — chơi thật.

File này ĐÃ VIẾT SẴN. Chạy được khi bạn làm xong 3 file kia.
Chạy: python main.py
"""
from ban_co import BanCo
from nguoi_choi import NguoiChoiNguoi, MayNgauNhien, MayThongMinh
from tro_choi import TroChoi


def chon(nhac, cac_lua_chon):
    """Hỏi tới khi nhận được một lựa chọn hợp lệ."""
    while True:
        print(nhac)
        for khoa, mo_ta in cac_lua_chon.items():
            print(f"  {khoa}. {mo_ta}")
        tra_loi = input("> ").strip()
        if tra_loi in cac_lua_chon:
            return tra_loi
        print("Lựa chọn không có. Thử lại.\n")


def mo_phong(so_van=100):
    """Cho hai máy đánh nhau nhiều ván để xem MayThongMinh mạnh thế nào."""
    ket_qua = {"X": 0, "O": 0, "hòa": 0}
    for seed in range(so_van):
        g = TroChoi(BanCo(),
                    MayThongMinh("Thông minh", "X", seed=seed),
                    MayNgauNhien("Ngẫu nhiên", "O", seed=seed + 1000),
                    im_lang=True)
        thang = g.chay()
        ket_qua["hòa" if thang is None else thang.quan] += 1

    print(f"\n{so_van} ván — Thông minh (X) vs Ngẫu nhiên (O):")
    print(f"  Thông minh thắng: {ket_qua['X']:>4}")
    print(f"  Ngẫu nhiên thắng: {ket_qua['O']:>4}")
    print(f"  Hòa:              {ket_qua['hòa']:>4}")
    if ket_qua["O"] == 0:
        print("\n  Máy thông minh không thua ván nào — logic chặn đúng.")
    else:
        print(f"\n  Máy thông minh thua {ket_qua['O']} ván — xem lại logic chặn.")


def main():
    print("=" * 50)
    print(" CARO / TIC-TAC-TOE")
    print("=" * 50)
    print()

    che_do = chon("Chọn chế độ:", {
        "1": "Người vs Máy thông minh",
        "2": "Người vs Máy ngẫu nhiên",
        "3": "Người vs Người",
        "4": "Mô phỏng 100 ván máy vs máy",
    })

    if che_do == "4":
        mo_phong()
        return

    co = chon("\nChọn bàn cờ:", {
        "1": "3x3, thắng 3 quân",
        "2": "5x5, thắng 4 quân",
    })
    ban_co = BanCo(3) if co == "1" else BanCo(5, can_de_thang=4)

    nguoi = NguoiChoiNguoi("Bạn", "X")
    if che_do == "1":
        doi_thu = MayThongMinh("Máy thông minh", "O")
    elif che_do == "2":
        doi_thu = MayNgauNhien("Máy ngẫu nhiên", "O")
    else:
        doi_thu = NguoiChoiNguoi("Người chơi 2", "O")

    print(f"\n{nguoi} đi trước. Nhập toạ độ dạng 'hàng cột', ví dụ: 1 1")
    print()

    thang = TroChoi(ban_co, nguoi, doi_thu).chay()

    print()
    if thang is None:
        print("Hòa.")
    else:
        print(f"{thang} thắng!")


if __name__ == "__main__":
    main()
