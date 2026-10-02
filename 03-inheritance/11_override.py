"""
TUẦN 5 — OVERRIDE (GHI ĐÈ METHOD)

Override = lớp con định nghĩa lại một method của lớp cha.
Đây là cơ chế làm cho đa hình (tuần 6) hoạt động.

Chạy: python 11_override.py
"""

# ---------------------------------------------------------------
# 1. OVERRIDE CƠ BẢN
# ---------------------------------------------------------------
print("1. OVERRIDE CƠ BẢN")


class ThongBao:
    def gui(self, noi_dung):
        return f"[chung] {noi_dung}"


class Email(ThongBao):
    def gui(self, noi_dung):                 # cùng tên, cùng tham số → override
        return f"[email] {noi_dung}"


class SMS(ThongBao):
    def gui(self, noi_dung):
        return f"[sms] {noi_dung[:20]}..."   # SMS giới hạn độ dài


for kenh in [ThongBao(), Email(), SMS()]:
    print(f"   {kenh.gui('Đơn hàng của bạn đã được xác nhận')}")

# Python không có từ khóa @Override như Java. Chỉ cần cùng tên method là đủ.
# Mặt tiêu cực: gõ sai tên method thì bạn tạo method MỚI thay vì override,
# và không có cảnh báo nào. Tuần 7 (abstract class) giải quyết việc này.


# ---------------------------------------------------------------
# 2. BA KIỂU OVERRIDE
# ---------------------------------------------------------------
print("\n2. BA KIỂU OVERRIDE")


class Luong:
    def tinh(self, co_ban):
        return co_ban


# Kiểu A — THAY THẾ hoàn toàn, không gọi cha
class LuongKhoan(Luong):
    def tinh(self, co_ban):
        return 10_000_000


# Kiểu B — MỞ RỘNG: gọi cha rồi thêm vào
class LuongCoThuong(Luong):
    def tinh(self, co_ban):
        return super().tinh(co_ban) + 2_000_000


# Kiểu C — TIỀN XỬ LÝ: sửa đầu vào rồi mới gọi cha
class LuongCoThue(Luong):
    def tinh(self, co_ban):
        return super().tinh(co_ban) * 0.9


print(f"   gốc:          {Luong().tinh(12_000_000):>12,.0f}")
print(f"   thay thế:     {LuongKhoan().tinh(12_000_000):>12,.0f}")
print(f"   mở rộng:      {LuongCoThuong().tinh(12_000_000):>12,.0f}")
print(f"   tiền xử lý:   {LuongCoThue().tinh(12_000_000):>12,.0f}")

# Kiểu B (gọi super() rồi thêm) là an toàn nhất: khi logic của cha đổi,
# con tự được cập nhật theo. Kiểu A dễ bị lạc hậu khi cha thay đổi.


# ---------------------------------------------------------------
# 3. OVERRIDE VÀ ĐÓNG GÓI CÙNG LÀM VIỆC
# ---------------------------------------------------------------
print("\n3. KẾT HỢP VỚI TUẦN 4")


class TaiKhoan:
    def __init__(self, chu, so_du=0):
        self.chu = chu
        self._so_du = so_du

    @property
    def so_du(self):
        return self._so_du

    def rut(self, tien):
        if tien > self._so_du:
            raise ValueError("Không đủ số dư")
        self._so_du -= tien
        return tien


class TaiKhoanCoPhi(TaiKhoan):
    PHI = 5_000

    def rut(self, tien):
        # Rút thêm phần phí — vẫn dùng kiểm tra số dư của lớp cha
        tong = tien + TaiKhoanCoPhi.PHI
        super().rut(tong)
        return tien              # người dùng chỉ nhận số tiền họ yêu cầu


tk = TaiKhoanCoPhi("Minh", 100_000)
nhan = tk.rut(50_000)
print(f"   rút 50,000 → nhận {nhan:,}, còn {tk.so_du:,} (đã trừ phí {TaiKhoanCoPhi.PHI:,})")

try:
    tk.rut(50_000)
except ValueError as e:
    print(f"   rút tiếp 50,000 bị chặn: {e}   ← kiểm tra của lớp cha vẫn chạy")


# ---------------------------------------------------------------
# 4. BẪY: LỚP CON LÀM HỎNG HỢP ĐỒNG CỦA LỚP CHA
# ---------------------------------------------------------------
print("\n4. BẪY: PHÁ HỢP ĐỒNG")


class DanhSach:
    def __init__(self):
        self._items = []

    def them(self, x):
        """Hợp đồng: luôn thêm được, luôn trả về số lượng mới."""
        self._items.append(x)
        return len(self._items)


class DanhSachChiSo(DanhSach):
    def them(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Chỉ nhận số")      # ← THẮT CHẶT điều kiện: nguy hiểm
        return super().them(x)


def xu_ly(ds, du_lieu):
    """Hàm này viết cho DanhSach, kỳ vọng mọi phần tử đều thêm được."""
    for x in du_lieu:
        ds.them(x)
    return "xong"


print(f"   với DanhSach:       {xu_ly(DanhSach(), [1, 'a', 2])}")
try:
    xu_ly(DanhSachChiSo(), [1, "a", 2])
except TypeError as e:
    print(f"   với DanhSachChiSo:  CRASH — {e}")

print("""
   Lớp con đã làm hỏng code vốn chạy đúng với lớp cha. Quy tắc:

     lớp con phải dùng thay được lớp cha ở MỌI nơi (Liskov Substitution).

   Nghĩa là override thì được, nhưng đừng THẮT CHẶT điều kiện đầu vào
   hay NỚI LỎNG cam kết đầu ra của lớp cha.

   Nếu bạn thấy mình cần thắt chặt như vậy → quan hệ is-a vốn đã sai,
   nên tách thành hai class riêng, không kế thừa.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_11_override.py
#
# 1. class Hinh với dien_tich() trả 0. Tạo HinhTron, HinhChuNhat, HinhTamGiac
#    override dien_tich(). In tổng diện tích của một list hỗn hợp.
# 2. class NguoiChoi với diem_thuong() = 10. Tạo NguoiChoiVIP (x2 điểm)
#    và NguoiChoiMoi (+5 điểm) dùng super()
# 3. class FileLog với ghi(msg). Tạo FileLogCoThoiGian thêm timestamp
#    vào đầu mỗi dòng bằng cách gọi super()
# 4. Tự tạo một ví dụ lớp con PHÁ hợp đồng của lớp cha, rồi sửa lại cho đúng
