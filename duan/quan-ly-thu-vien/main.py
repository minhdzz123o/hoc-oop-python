"""
Dự án 1 — kịch bản sử dụng.

File này ĐÃ VIẾT SẴN. Nó chỉ chạy được khi bạn làm xong 3 file kia.
Chạy: python main.py
"""
import os
import tempfile

from tai_lieu import Sach, Bao, DiaDVD
from thanh_vien import ThanhVienThuong, ThanhVienVIP
from thu_vien import ThuVien


def tao_thu_vien_mau():
    tv = ThuVien("Thư viện Quốc gia")

    for ma, tieu_de, tac_gia in [
        ("S01", "Clean Code", "Robert Martin"),
        ("S02", "Refactoring", "Martin Fowler"),
        ("S03", "The Pragmatic Programmer", "Hunt & Thomas"),
    ]:
        tv.them_tai_lieu(Sach(ma, tieu_de, tac_gia))

    tv.them_tai_lieu(Bao("B01", "Tuổi Trẻ"))
    tv.them_tai_lieu(Bao("B02", "Thanh Niên"))
    tv.them_tai_lieu(DiaDVD("D01", "Inception", "Christopher Nolan"))

    tv.them_thanh_vien(ThanhVienThuong("TV01", "Minh"))
    tv.them_thanh_vien(ThanhVienThuong("TV02", "Hùng"))
    tv.them_thanh_vien(ThanhVienVIP("TV03", "Lan"))
    return tv


def vach(tieu_de):
    print()
    print("=" * 62)
    print(f" {tieu_de}")
    print("=" * 62)


def main():
    tv = tao_thu_vien_mau()

    vach("KHO BAN ĐẦU")
    for tl in tv.co_san():
        print(f"  {tl.mo_ta()}")

    vach("CHO MƯỢN")
    for ma_tv, ma_tl in [("TV01", "S01"), ("TV01", "B01"),
                         ("TV03", "S02"), ("TV03", "D01"), ("TV02", "S03")]:
        print(f"  {tv.cho_muon(ma_tv, ma_tl)}")

    vach("CÁC TRƯỜNG HỢP BỊ CHẶN")
    cac_thu = [
        ("TV02", "S01", "mượn cái đang có người mượn"),
        ("KHONG_CO", "B02", "thành viên không tồn tại"),
        ("TV01", "KHONG_CO", "tài liệu không tồn tại"),
    ]
    for ma_tv, ma_tl, ly_do in cac_thu:
        try:
            tv.cho_muon(ma_tv, ma_tl)
            print(f"  LỖI THIẾT KẾ: đáng lẽ phải chặn ({ly_do})")
        except ValueError as e:
            print(f"  bị chặn ({ly_do}): {e}")

    # Minh (thường) đã mượn 2, mượn thêm 1 nữa là đủ 3, cái thứ 4 phải bị chặn
    tv.cho_muon("TV01", "B02")
    try:
        tv.cho_muon("TV01", "S01")
        print("  LỖI THIẾT KẾ: đáng lẽ chặn vì quá hạn mức")
    except ValueError as e:
        print(f"  bị chặn (quá hạn mức): {e}")

    vach("TRẢ VÀ TÍNH PHÍ TRỄ")
    print(f"  Minh trả S01 đúng hạn:      {tv.tra('TV01', 'S01', 0):>10,.0f} đ")
    print(f"  Minh trả B01 trễ 5 ngày:    {tv.tra('TV01', 'B01', 5):>10,.0f} đ")
    print(f"     (báo phí gấp 4 lần sách)")
    print(f"  Lan (VIP) trả S02 trễ 10 ngày: {tv.tra('TV03', 'S02', 10):>7,.0f} đ")
    print(f"     (VIP miễn phí trễ)")

    vach("BÁO CÁO")
    print(tv.bao_cao())

    vach("LƯU VÀ TẢI LẠI")
    duong_dan = os.path.join(tempfile.gettempdir(), "thu_vien.json")
    tv.luu(duong_dan)
    print(f"  đã lưu {len(tv)} tài liệu")

    tv2 = ThuVien.tai(duong_dan)
    print(f"  tải lại: {tv2!r}")
    print(f"  có sẵn trước: {len(tv.co_san())}, sau khi tải: {len(tv2.co_san())}")
    giong = (len(tv2) == len(tv)
             and len(tv2.co_san()) == len(tv.co_san())
             and tv2.ten == tv.ten)
    print(f"  khớp với bản gốc: {giong}")
    os.remove(duong_dan)

    print()
    print("Xong. Nếu mọi mục trên chạy đúng, dự án 1 hoàn thành.")
    print("Thử phần MỞ RỘNG trong README.md, hoặc sang duan/game-caro/")


if __name__ == "__main__":
    main()
