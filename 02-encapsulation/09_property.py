"""
TUẦN 4 — @property: CÁCH ĐÓNG GÓI CỦA PYTHON

@property cho bạn viết `n.ten = "Minh"` nhưng vẫn chạy được code kiểm tra
ở giữa. Người dùng thấy nó như attribute bình thường, bên trong là method.

Đây là nét riêng của Python mà Java/C# không có theo cách này.

Chạy: python 09_property.py
"""

# ---------------------------------------------------------------
# 1. @property CƠ BẢN — chỉ cho đọc
# ---------------------------------------------------------------
print("1. PROPERTY CHỈ ĐỌC")


class HinhTron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    @property
    def dien_tich(self):
        """Tính mỗi lần đọc. Gọi KHÔNG CÓ dấu () — như attribute."""
        return 3.14159 * self.ban_kinh ** 2

    @property
    def chu_vi(self):
        return 2 * 3.14159 * self.ban_kinh


h = HinhTron(3)
print(f"   h.dien_tich = {h.dien_tich:.2f}   ← không có dấu ()")
print(f"   h.chu_vi    = {h.chu_vi:.2f}")

h.ban_kinh = 5
print(f"   đổi bán kính thành 5 → diện tích {h.dien_tich:.2f}  ← tự cập nhật")

# Không có setter → không gán được, được bảo vệ tự động:
try:
    h.dien_tich = 100
except AttributeError as e:
    print(f"   gán h.dien_tich → bị chặn: {e}")

# Khi nào dùng property thay vì method?
#   - Giá trị DẪN XUẤT từ dữ liệu khác, tính nhanh → property (dien_tich)
#   - Có tác dụng phụ, hoặc tính tốn kém, hoặc cần tham số → method


# ---------------------------------------------------------------
# 2. @property + SETTER — kiểm tra khi gán
# ---------------------------------------------------------------
print("\n2. PROPERTY CÓ SETTER")


class TaiKhoan:
    def __init__(self, chu, so_du=0):
        self.chu = chu
        self.so_du = so_du          # gọi SETTER bên dưới, nên được kiểm tra luôn

    @property
    def so_du(self):
        return self._so_du

    @so_du.setter
    def so_du(self, gia_tri):
        if not isinstance(gia_tri, (int, float)):
            raise TypeError("Số dư phải là số")
        if gia_tri < 0:
            raise ValueError(f"Số dư không được âm (nhận {gia_tri})")
        self._so_du = gia_tri

    def nap(self, tien):
        if tien <= 0:
            raise ValueError("Số tiền nạp phải dương")
        self.so_du = self.so_du + tien      # đi qua setter → vẫn được kiểm tra


tk = TaiKhoan("Minh", 1000)
print(f"   số dư: {tk.so_du:,}")

tk.nap(500)
print(f"   sau nap(500): {tk.so_du:,}")

tk.so_du = 2000                     # gán trực tiếp VẪN ĐƯỢC, nhưng có kiểm tra
print(f"   gán 2000 (hợp lệ): {tk.so_du:,}")

for gia_tri in [-500, "nhiều"]:
    try:
        tk.so_du = gia_tri
    except (ValueError, TypeError) as e:
        print(f"   gán {gia_tri!r} bị chặn: {e}")

print(f"   số dư cuối: {tk.so_du:,}   ← không bị phá")

# So với file 08: giao diện gọn như attribute công khai, an toàn như method.
# Đây là lý do Python không cần get_x()/set_x().


# ---------------------------------------------------------------
# 3. VÍ DỤ ĐẸP: TỰ ĐỘNG CHUYỂN ĐỔI ĐƠN VỊ
# ---------------------------------------------------------------
print("\n3. CHUYỂN ĐỔI ĐƠN VỊ TỰ ĐỘNG")


class NhietDo:
    """Lưu một giá trị duy nhất (Celsius), nhưng đọc/ghi được cả hai thang."""

    DO_0_TUYET_DOI = -273.15

    def __init__(self, celsius=0.0):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, gia_tri):
        if gia_tri < NhietDo.DO_0_TUYET_DOI:
            raise ValueError(f"Không thể lạnh hơn {NhietDo.DO_0_TUYET_DOI}°C")
        self._celsius = gia_tri

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, f):
        self.celsius = (f - 32) * 5 / 9      # đi qua setter celsius → vẫn validate

    @property
    def kelvin(self):
        return self._celsius - NhietDo.DO_0_TUYET_DOI


n = NhietDo(25)
print(f"   25°C = {n.fahrenheit}°F = {n.kelvin}K")

n.fahrenheit = 212                   # ghi bằng thang F
print(f"   gán 212°F → {n.celsius}°C   ← chỉ có một giá trị được lưu")

try:
    n.celsius = -300
except ValueError as e:
    print(f"   gán -300°C bị chặn: {e}")

try:
    n.fahrenheit = -500             # dưới độ 0 tuyệt đối
except ValueError as e:
    print(f"   gán -500°F cũng bị chặn: {e}")
    print("   ← vì setter fahrenheit đi qua setter celsius, không lặp code validate")


# ---------------------------------------------------------------
# 4. ĐỪNG LẠM DỤNG @property
# ---------------------------------------------------------------
print("\n4. KHI NÀO KHÔNG CẦN PROPERTY")

print("""   SAI — property không làm gì ngoài gán, thừa hoàn toàn:

       @property
       def ten(self):
           return self._ten

       @ten.setter
       def ten(self, v):
           self._ten = v

   Cứ để  self.ten = ten  là xong. Python cho phép đổi sang property
   SAU NÀY mà không phá code của người dùng — khác với Java, nơi bạn
   buộc phải viết getter từ đầu để phòng xa.

   Dùng @property khi:
   - cần kiểm tra giá trị trước khi gán       (so_du, celsius)
   - giá trị được TÍNH ra từ dữ liệu khác     (dien_tich, kelvin)
   - chỉ muốn cho đọc, không cho ghi          (property không có setter)
   - cần giữ tương thích khi logic bên trong đổi""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_09_property.py
#
# 1. class HinhVuong(canh): property dien_tich, chu_vi (chỉ đọc);
#    setter của canh chặn số <= 0
# 2. class NguoiDung: property email, setter chặn chuỗi không có "@" và "."
#    Thêm property ten_mien (chỉ đọc) trả về phần sau dấu @
# 3. class KhoangThoiGian(giay): property phut, gio đọc/ghi được cả ba,
#    nhưng bên trong chỉ lưu một giá trị
# 4. class SanPham(gia, giam_gia): property gia_cuoi (chỉ đọc) = gia*(1-giam_gia);
#    setter giam_gia chặn ngoài khoảng 0-1
