"""
TUẦN 3 — CLASS VÀ OBJECT

class  = cái khuôn (bản thiết kế)
object = vật được tạo ra từ khuôn (instance)

Một class, tạo được vô số object. Như một khuôn bánh làm được nhiều bánh.

Chạy: python 05_class_object.py
"""

# ---------------------------------------------------------------
# 1. CLASS ĐẦU TIÊN
# ---------------------------------------------------------------
print("1. CLASS ĐẦU TIÊN")


class SinhVien:
    """Tên class viết kiểu PascalCase: SinhVien, TaiKhoanNganHang."""

    def __init__(self, ten, tuoi):
        # __init__ chạy TỰ ĐỘNG khi tạo object. Nó không phải "hàm tạo object",
        # nó là hàm KHỞI TẠO GIÁ TRỊ cho object vừa được tạo.
        self.ten = ten          # self.ten là attribute của object này
        self.tuoi = tuoi

    def gioi_thieu(self):
        # Mọi method đều có `self` là tham số ĐẦU TIÊN.
        # self = chính object đang gọi method này.
        return f"Tôi là {self.ten}, {self.tuoi} tuổi"


# Tạo object — gọi tên class như gọi hàm. KHÔNG dùng `new` như Java.
sv1 = SinhVien("Minh", 20)
sv2 = SinhVien("Lan", 21)

print(f"   {sv1.gioi_thieu()}")
print(f"   {sv2.gioi_thieu()}")

# Hai object độc lập, mỗi object có dữ liệu riêng:
sv1.tuoi = 25
print(f"   sau khi đổi tuổi sv1: sv1={sv1.tuoi}, sv2={sv2.tuoi}  ← sv2 không đổi")

print(f"   sv1 là object của class: {type(sv1).__name__}")
print(f"   sv1 có phải SinhVien: {isinstance(sv1, SinhVien)}")


# ---------------------------------------------------------------
# 2. VIẾT LẠI BÀI TUẦN 2 THÀNH CLASS — so sánh trực tiếp
# ---------------------------------------------------------------
print("\n2. SO SÁNH VỚI CÁCH DÙNG DICT (tuần 2)")


class TaiKhoan:
    def __init__(self, chu_so_huu, so_du=0):
        self.chu_so_huu = chu_so_huu
        self.so_du = so_du
        self.lich_su = []           # tuần 4 ta sẽ bảo vệ các attribute này

    def nap(self, tien):
        if tien <= 0:
            raise ValueError("Số tiền nạp phải dương")
        self.so_du += tien
        self.lich_su.append(f"nạp {tien}")

    def rut(self, tien):
        if tien > self.so_du:
            raise ValueError("Không đủ số dư")
        self.so_du -= tien
        self.lich_su.append(f"rút {tien}")


tk = TaiKhoan("Minh", 1000)
tk.nap(500)                     # so với: nap(tk, 500)
tk.rut(200)
print(f"   {tk.chu_so_huu}: {tk.so_du}")
print(f"   lịch sử: {tk.lich_su}")

# Lợi ích thấy ngay: gõ sai tên attribute thì bị phát hiện LẬP TỨC
try:
    print(tk.sodu)              # thiếu dấu gạch dưới
except AttributeError as e:
    print(f"   gõ sai attribute → AttributeError: {e}")
    print("   ← với dict thì lỗi này im lặng (xem lại file 04)")


# ---------------------------------------------------------------
# 3. BẪY LỚN: CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE
# ---------------------------------------------------------------
print("\n3. BẪY: CLASS ATTRIBUTE vs INSTANCE ATTRIBUTE")


class LopSai:
    danh_sach = []              # ❌ khai ở THÂN CLASS → MỌI object dùng chung!

    def __init__(self, ten):
        self.ten = ten

    def them(self, sv):
        self.danh_sach.append(sv)


a = LopSai("K20A")
b = LopSai("K20B")
a.them("Minh")
b.them("Lan")

print(f"   lớp A: {a.danh_sach}")
print(f"   lớp B: {b.danh_sach}")
print("   ← HAI LỚP DÙNG CHUNG MỘT LIST. Đây gần như luôn là bug.")


class LopDung:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach = []    # ✅ khai trong __init__ → mỗi object một list riêng

    def them(self, sv):
        self.danh_sach.append(sv)


c = LopDung("K20A")
d = LopDung("K20B")
c.them("Minh")
d.them("Lan")
print(f"   đúng — lớp A: {c.danh_sach}, lớp B: {d.danh_sach}")

# Quy tắc đơn giản:
#   Dữ liệu RIÊNG của từng object  → khai trong __init__ với self.
#   Hằng số / giá trị DÙNG CHUNG   → khai ở thân class (xem mục 4)
#
# Đây chính là cái bẫy mutable ở file 02_ham.py, xuất hiện lại dưới dạng khác.


# ---------------------------------------------------------------
# 4. CLASS ATTRIBUTE DÙNG ĐÚNG CHỖ
# ---------------------------------------------------------------
print("\n4. CLASS ATTRIBUTE DÙNG ĐÚNG")


class HinhTron:
    PI = 3.14159            # hằng số, dùng chung cho mọi hình tròn — ĐÚNG
    so_hinh_da_tao = 0      # bộ đếm toàn class — cũng là một cách dùng đúng

    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
        HinhTron.so_hinh_da_tao += 1     # cập nhật qua TÊN CLASS, không qua self

    def dien_tich(self):
        return HinhTron.PI * self.ban_kinh ** 2


h1 = HinhTron(2)
h2 = HinhTron(3)
print(f"   diện tích h1: {h1.dien_tich():.2f}")
print(f"   diện tích h2: {h2.dien_tich():.2f}")
print(f"   đã tạo {HinhTron.so_hinh_da_tao} hình tròn")
print(f"   PI dùng chung: {HinhTron.PI}")


# ---------------------------------------------------------------
# 5. OBJECT NẰM TRONG LIST — chỗ list gặp class
# ---------------------------------------------------------------
print("\n5. LIST CỦA OBJECT")

lop = [
    SinhVien("Minh", 20),
    SinhVien("Lan", 21),
    SinhVien("Hùng", 19),
]

for sv in lop:
    print(f"   {sv.gioi_thieu()}")

# Mọi thứ học ở tuần 2 vẫn dùng được, chỉ thay sv["ten"] thành sv.ten
tre_nhat = min(lop, key=lambda sv: sv.tuoi)
print(f"   trẻ nhất: {tre_nhat.ten}")
print(f"   tuổi TB: {sum(sv.tuoi for sv in lop) / len(lop):.1f}")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_05_class.py
#
# 1. class HinhChuNhat(rong, cao) với dien_tich(), chu_vi(), la_hinh_vuong()
# 2. class Sach(tieu_de, tac_gia, so_trang) với mo_ta() trả về chuỗi đẹp
# 3. class BoDem: đếm từ 0, có tang(), giam(), reset(), xem()
# 4. Viết class ChuoiSo với một attribute list. Chứng minh bằng code rằng
#    khai list ở thân class là sai, bằng cách tạo 2 object và thêm vào mỗi cái.
