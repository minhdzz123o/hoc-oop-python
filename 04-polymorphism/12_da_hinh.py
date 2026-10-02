"""
TUẦN 6 — POLYMORPHISM (ĐA HÌNH)

Đây là phần có giá trị nhất của OOP. Nếu bạn chỉ học tới kế thừa rồi dừng,
bạn đã bỏ qua lý do chính vì sao OOP tồn tại.

Đa hình = GỌI CÙNG MỘT TÊN METHOD trên nhiều loại object khác nhau,
và mỗi object tự biết phải làm gì.

Chạy: python 12_da_hinh.py
"""

import math

# ---------------------------------------------------------------
# 1. VẤN ĐỀ MÀ ĐA HÌNH GIẢI QUYẾT
# ---------------------------------------------------------------
print("1. VẤN ĐỀ: CHUỖI if/elif DÀI VÔ TẬN")

print("""   Không có đa hình, bạn viết thế này:

       def dien_tich(hinh):
           if hinh["loai"] == "tron":
               return 3.14 * hinh["r"] ** 2
           elif hinh["loai"] == "chu_nhat":
               return hinh["rong"] * hinh["cao"]
           elif hinh["loai"] == "tam_giac":
               return hinh["day"] * hinh["cao"] / 2
           # ... thêm hình mới = sửa hàm này
           # ... và sửa chu_vi(), và sửa ve(), và sửa mo_ta()...

   Thêm một loại hình = phải tìm và sửa MỌI hàm có chuỗi if này.
   Quên một chỗ = bug. Đây là nguồn gốc của phần lớn code khó bảo trì.""")


# ---------------------------------------------------------------
# 2. ĐA HÌNH: MỖI LOẠI TỰ BIẾT CÁCH TÍNH
# ---------------------------------------------------------------
print("2. ĐA HÌNH")


class Hinh:
    def __init__(self, ten):
        self.ten = ten

    def dien_tich(self):
        raise NotImplementedError("Lớp con phải tự cài đặt")

    def chu_vi(self):
        raise NotImplementedError("Lớp con phải tự cài đặt")

    def mo_ta(self):
        # Method này viết MỘT LẦN, chạy đúng cho mọi lớp con
        return f"{self.ten}: S={self.dien_tich():.2f}, P={self.chu_vi():.2f}"


class HinhTron(Hinh):
    def __init__(self, r):
        super().__init__("Hình tròn")
        self.r = r

    def dien_tich(self):
        return math.pi * self.r ** 2

    def chu_vi(self):
        return 2 * math.pi * self.r


class HinhChuNhat(Hinh):
    def __init__(self, rong, cao):
        super().__init__("Hình chữ nhật")
        self.rong = rong
        self.cao = cao

    def dien_tich(self):
        return self.rong * self.cao

    def chu_vi(self):
        return 2 * (self.rong + self.cao)


class HinhTamGiac(Hinh):
    def __init__(self, a, b, c):
        super().__init__("Hình tam giác")
        self.a, self.b, self.c = a, b, c

    def dien_tich(self):
        p = self.chu_vi() / 2                       # công thức Heron
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def chu_vi(self):
        return self.a + self.b + self.c


# ĐÂY LÀ ĐIỂM QUAN TRỌNG NHẤT CỦA CẢ LỘ TRÌNH:
hinh_list = [HinhTron(3), HinhChuNhat(4, 5), HinhTamGiac(3, 4, 5)]

for h in hinh_list:
    print(f"   {h.mo_ta()}")

print(f"   tổng diện tích: {sum(h.dien_tich() for h in hinh_list):.2f}")
print(f"   lớn nhất: {max(hinh_list, key=lambda h: h.dien_tich()).ten}")

print("""
   Nhìn vòng lặp trên: KHÔNG CÓ MỘT CÂU if NÀO về loại hình.
   Vòng lặp không cần biết nó đang xử lý hình gì.

   Thêm HinhThang? Chỉ cần viết class mới. Vòng lặp này, mo_ta(),
   hàm tổng diện tích — không sửa một dòng nào.

   Đó là lợi ích thật của OOP: THÊM TÍNH NĂNG MÀ KHÔNG SỬA CODE CŨ.""")


# ---------------------------------------------------------------
# 3. VÍ DỤ THỰC TẾ: XUẤT BÁO CÁO NHIỀU ĐỊNH DẠNG
# ---------------------------------------------------------------
print("3. VÍ DỤ THỰC TẾ: XUẤT BÁO CÁO")


class BoXuat:
    duoi_file = "txt"

    def xuat(self, du_lieu):
        raise NotImplementedError

    def luu(self, du_lieu, ten_file):
        """Viết một lần, dùng cho mọi định dạng."""
        noi_dung = self.xuat(du_lieu)
        return f"đã ghi {len(noi_dung)} ký tự vào {ten_file}.{self.duoi_file}"


class XuatCSV(BoXuat):
    duoi_file = "csv"

    def xuat(self, du_lieu):
        cot = list(du_lieu[0].keys())
        dong = [",".join(cot)]
        for hang in du_lieu:
            dong.append(",".join(str(hang[c]) for c in cot))
        return "\n".join(dong)


class XuatJSON(BoXuat):
    duoi_file = "json"

    def xuat(self, du_lieu):
        import json
        return json.dumps(du_lieu, ensure_ascii=False, indent=2)


class XuatBang(BoXuat):
    duoi_file = "txt"

    def xuat(self, du_lieu):
        cot = list(du_lieu[0].keys())
        rong = {c: max(len(c), *(len(str(h[c])) for h in du_lieu)) for c in cot}
        dong = [" | ".join(c.ljust(rong[c]) for c in cot)]
        dong.append("-+-".join("-" * rong[c] for c in cot))
        for hang in du_lieu:
            dong.append(" | ".join(str(hang[c]).ljust(rong[c]) for c in cot))
        return "\n".join(dong)


du_lieu = [
    {"ten": "Minh", "diem": 8.5},
    {"ten": "Lan", "diem": 9.0},
]

for bo in [XuatCSV(), XuatJSON(), XuatBang()]:
    print(f"\n   --- {type(bo).__name__} ---")
    for dong in bo.xuat(du_lieu).split("\n"):
        print(f"   {dong}")

print()
for bo in [XuatCSV(), XuatJSON(), XuatBang()]:
    print(f"   {bo.luu(du_lieu, 'bao_cao')}")

print("""
   Hàm dùng chúng không cần biết định dạng nào:

       def tao_bao_cao(bo_xuat, du_lieu):
           return bo_xuat.luu(du_lieu, "bao_cao")

   Thêm XuatPDF, XuatExcel — hàm này không đổi.
   Đây là nền tảng của Strategy pattern, thứ bạn sẽ gặp khi học design patterns.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_12_da_hinh.py
#
# 1. class PhuongTien với thoi_gian_di(km). Tạo XeDap (15km/h), XeMay (40),
#    OTo (60), MayBay (800 nhưng +2 giờ làm thủ tục).
#    Viết hàm nhanh_nhat(list_phuong_tien, km) trả về loại nhanh nhất.
# 2. class BoLoc với ap_dung(danh_sach). Tạo LocSoChan, LocSoNguyenTo,
#    LocLonHon(n). Áp dụng lần lượt nhiều bộ lọc lên một list.
# 3. class ThanhToan với xu_ly(so_tien). Tạo TheTinDung (phí 2%),
#    ViDienTu (phí 0.5%), ChuyenKhoan (phí cố định 5000).
#    In bảng so sánh phí cho số tiền 1,000,000.
# 4. Viết lại bài 1 bằng chuỗi if/elif, rồi so sánh: thêm một loại
#    phương tiện mới thì mỗi cách phải sửa bao nhiêu chỗ?
