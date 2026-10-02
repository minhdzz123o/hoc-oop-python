"""
TUẦN 3 — METHOD: HÀM GẮN VỚI DỮ LIỆU

Nếu bạn nhớ một câu từ tuần 3, hãy nhớ câu này:

    method = hàm + quyền truy cập dữ liệu của object qua self

Chạy: python 07_method_vs_function.py
"""

# ---------------------------------------------------------------
# 1. CÙNG MỘT LOGIC, HAI CÁCH VIẾT
# ---------------------------------------------------------------
print("1. HÀM RỜI vs METHOD")


# Cách hàm rời: phải truyền dữ liệu vào
def dien_tich_hcn(rong, cao):
    return rong * cao


print(f"   hàm rời:  dien_tich_hcn(3, 4) = {dien_tich_hcn(3, 4)}")


# Cách method: dữ liệu đã nằm trong object
class HinhChuNhat:
    def __init__(self, rong, cao):
        self.rong = rong
        self.cao = cao

    def dien_tich(self):
        return self.rong * self.cao      # không cần tham số, lấy từ self

    def chu_vi(self):
        return 2 * (self.rong + self.cao)

    def phong_to(self, he_so):
        """Method có thể THAY ĐỔI trạng thái object."""
        self.rong *= he_so
        self.cao *= he_so

    def la_hinh_vuong(self):
        return self.rong == self.cao


h = HinhChuNhat(3, 4)
print(f"   method:   h.dien_tich()      = {h.dien_tich()}")
print(f"             h.chu_vi()         = {h.chu_vi()}")
print(f"             h.la_hinh_vuong()  = {h.la_hinh_vuong()}")

h.phong_to(2)
print(f"   sau phong_to(2): {h.rong}x{h.cao}, diện tích {h.dien_tich()}")
print("   ← object GHI NHỚ trạng thái giữa các lời gọi. Hàm rời không làm được.")


# ---------------------------------------------------------------
# 2. HAI LOẠI METHOD
# ---------------------------------------------------------------
print("\n2. HAI LOẠI METHOD")

print("""   Phân biệt này rất hữu ích khi thiết kế class:

   a) Method TRUY VẤN (query)  — đọc dữ liệu, trả về giá trị, không sửa gì
      ví dụ: dien_tich(), chu_vi(), la_hinh_vuong()

   b) Method HÀNH ĐỘNG (command) — thay đổi trạng thái object
      ví dụ: phong_to(), nap(), rut()

   Nguyên tắc tốt: một method nên làm MỘT trong hai, đừng làm cả hai.
   Method vừa sửa dữ liệu vừa trả giá trị rất dễ gây lỗi khó tìm.""")


# ---------------------------------------------------------------
# 3. METHOD GỌI METHOD KHÁC
# ---------------------------------------------------------------
print("\n3. METHOD GỌI METHOD KHÁC")


class DonHang:
    THUE = 0.1

    def __init__(self):
        self.mon = []          # list các tuple (tên, giá, số lượng)

    def them(self, ten, gia, sl=1):
        self.mon.append((ten, gia, sl))

    def tien_hang(self):
        return sum(gia * sl for _, gia, sl in self.mon)

    def tien_thue(self):
        return self.tien_hang() * DonHang.THUE      # gọi method khác qua self

    def tong_cong(self):
        return self.tien_hang() + self.tien_thue()

    def hoa_don(self):
        dong = []
        for ten, gia, sl in self.mon:
            dong.append(f"   {ten:12} {gia:>10,.0f} x{sl}")
        dong.append(f"   {'tiền hàng':12} {self.tien_hang():>10,.0f}")
        dong.append(f"   {'thuế 10%':12} {self.tien_thue():>10,.0f}")
        dong.append(f"   {'TỔNG':12} {self.tong_cong():>10,.0f}")
        return "\n".join(dong)


d = DonHang()
d.them("Bàn", 1200000)
d.them("Ghế", 350000, 4)
print(d.hoa_don())

# Mỗi method làm một việc nhỏ, hoa_don() chỉ ghép lại.
# Đây chính là "tách bài toán thành hàm nhỏ" ở file 02, nay trong class.


# ---------------------------------------------------------------
# 4. KHI NÀO KHÔNG CẦN CLASS
# ---------------------------------------------------------------
print("\n4. KHI NÀO KHÔNG CẦN CLASS")

print("""   OOP không phải lúc nào cũng đúng. Đừng viết class khi:

   - Chỉ có một hàm thuần: tinh_bmi(cao, nang) → cứ để là hàm
   - Class không có trạng thái: nếu mọi method đều không dùng self,
     thì đó là một đống hàm bị gói vào class một cách vô ích
   - Dữ liệu chỉ đọc một lần rồi bỏ

   Dấu hiệu NÊN dùng class:
   - Có dữ liệu cần giữ qua nhiều lời gọi  (tài khoản, giỏ hàng, bàn cờ)
   - Có nhiều hàm cùng thao tác trên một bộ dữ liệu
   - Cần nhiều bản của cùng một thứ        (nhiều sinh viên, nhiều đơn hàng)
   - Cần bảo vệ dữ liệu khỏi bị sửa bừa    (tuần 4)""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_07_method.py
#
# 1. class MayTinhBoTui: có cong(x), tru(x), nhan(x), chia(x) tác động lên
#    một giá trị hiện tại, cộng thêm xoa() và ket_qua()
#    → gọi được kiểu: mt.cong(5).nhan(3)  (gợi ý: return self)
# 2. class ChuoiVanBan(noi_dung): dem_tu(), dem_ky_tu(), viet_hoa_dau_cau()
# 3. class ThoiKhoaBieu: them_tiet(thu, mon), xem_thu(thu), tong_tiet()
# 4. Chỉ ra trong 3 class trên, method nào là TRUY VẤN, method nào là HÀNH ĐỘNG
