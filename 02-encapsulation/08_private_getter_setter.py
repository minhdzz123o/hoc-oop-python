"""
TUẦN 4 — ENCAPSULATION (ĐÓNG GÓI)

Đây là lời giải cho VẤN ĐỀ 1 ở file 04_dict_lam_doi_tuong.py:
dữ liệu không được bảo vệ.

Ý tưởng: object tự quyết định ai được chạm vào dữ liệu của nó, và chạm thế nào.

Chạy: python 08_private_getter_setter.py
"""

# ---------------------------------------------------------------
# 1. SỰ THẬT VỀ private TRONG PYTHON
# ---------------------------------------------------------------
print("1. PYTHON KHÔNG CÓ private THẬT")

print("""   Java/C# có từ khóa private chặn hẳn ở mức ngôn ngữ.
   Python KHÔNG. Python chỉ có quy ước:

     self.ten        công khai  — dùng thoải mái
     self._ten       "nội bộ"   — quy ước: đừng chạm từ ngoài
     self.__ten      name mangling — Python đổi tên để khó chạm hơn

   Triết lý Python: "we are all consenting adults" — tin người dùng code
   của bạn là người hiểu chuyện, chỉ cần BÁO HIỆU rõ, không cần cấm.""")


class ViDu:
    def __init__(self):
        self.cong_khai = "ai cũng dùng được"
        self._noi_bo = "đừng chạm từ ngoài"
        self.__rieng = "bị đổi tên"


v = ViDu()
print(f"\n   v.cong_khai  = {v.cong_khai}")
print(f"   v._noi_bo    = {v._noi_bo}   ← vẫn truy cập được! chỉ là quy ước")

try:
    print(v.__rieng)
except AttributeError:
    print("   v.__rieng    → AttributeError")
    print(f"   nhưng: v._ViDu__rieng = {v._ViDu__rieng}")
    print("   ← đây là name mangling, không phải bảo mật")

# Nên dùng gì? Trong thực tế: dùng MỘT dấu gạch dưới `_` là đủ.
# `__` hai gạch chỉ dùng khi bạn thật sự cần tránh trùng tên khi kế thừa.


# ---------------------------------------------------------------
# 2. VÌ SAO CẦN ĐÓNG GÓI — ví dụ tài khoản ngân hàng
# ---------------------------------------------------------------
print("\n2. TAI KHOẢN NGÂN HÀNG — KHÔNG ĐÓNG GÓI")


class TaiKhoanHo:
    """Phiên bản KHÔNG bảo vệ — xem nó hỏng thế nào."""

    def __init__(self, chu, so_du=0):
        self.chu = chu
        self.so_du = so_du          # công khai → ai cũng gán được

    def rut(self, tien):
        if tien > self.so_du:
            raise ValueError("Không đủ số dư")
        self.so_du -= tien


t = TaiKhoanHo("Minh", 1000)
t.so_du = -500_000              # không ai chặn
print(f"   gán so_du = -500000 → {t.so_du}")
print("   ← số dư âm. Mọi kiểm tra trong rut() thành vô nghĩa.")


print("\n   TAI KHOẢN NGÂN HÀNG — CÓ ĐÓNG GÓI")


class TaiKhoan:
    """Phiên bản ĐÚNG — số dư chỉ đổi được qua nap() và rut()."""

    def __init__(self, chu, so_du=0):
        if so_du < 0:
            raise ValueError("Số dư ban đầu không được âm")
        self.chu = chu
        self._so_du = so_du        # dấu _ : báo hiệu "nội bộ, đừng chạm"
        self._lich_su = []

    # --- method TRUY VẤN: cho đọc, không cho ghi ---
    def xem_so_du(self):
        return self._so_du

    def xem_lich_su(self):
        return list(self._lich_su)   # trả BẢN COPY, không trả list gốc!

    # --- method HÀNH ĐỘNG: cửa duy nhất để đổi số dư ---
    def nap(self, tien):
        if tien <= 0:
            raise ValueError("Số tiền nạp phải dương")
        self._so_du += tien
        self._lich_su.append(f"nạp {tien:,}")

    def rut(self, tien):
        if tien <= 0:
            raise ValueError("Số tiền rút phải dương")
        if tien > self._so_du:
            raise ValueError(f"Không đủ số dư (có {self._so_du:,}, rút {tien:,})")
        self._so_du -= tien
        self._lich_su.append(f"rút {tien:,}")


tk = TaiKhoan("Minh", 1000)
tk.nap(500)
tk.rut(200)
print(f"   số dư: {tk.xem_so_du():,}")
print(f"   lịch sử: {tk.xem_lich_su()}")

for hanh_dong, tien in [("nap", -100), ("rut", 999999), ("rut", 0)]:
    try:
        getattr(tk, hanh_dong)(tien)
    except ValueError as e:
        print(f"   {hanh_dong}({tien}) bị chặn: {e}")

print(f"   số dư sau các lần bị chặn: {tk.xem_so_du():,}   ← không đổi")


# ---------------------------------------------------------------
# 3. TRẢ VỀ BẢN COPY — lỗi rất hay bị bỏ qua
# ---------------------------------------------------------------
print("\n3. RÒ RỈ DỮ LIỆU QUA LIST")


class LopHoc:
    def __init__(self):
        self._sv = ["Minh", "Lan"]

    def danh_sach_ho(self):
        return self._sv              # SAI: trả list GỐC

    def danh_sach_kin(self):
        return list(self._sv)        # ĐÚNG: trả bản copy


l = LopHoc()
l.danh_sach_ho().append("KẺ XÂM NHẬP")
print(f"   sau khi sửa list trả về: {l._sv}")
print("   ← dữ liệu nội bộ bị sửa từ bên ngoài, dù có dấu _")

l2 = LopHoc()
l2.danh_sach_kin().append("KẺ XÂM NHẬP")
print(f"   với bản copy: {l2._sv}   ← an toàn")

# Nhớ lại file 02_ham.py mục 4: list là mutable, trả nó ra là trao quyền sửa.


# ---------------------------------------------------------------
# 4. GETTER/SETTER KIỂU JAVA — ĐỪNG VIẾT TRONG PYTHON
# ---------------------------------------------------------------
print("\n4. BẪY: GETTER/SETTER KIỂU JAVA")

print("""   Nhiều người học OOP từ Java rồi viết trong Python:

       class Nguoi:
           def __init__(self, ten):
               self._ten = ten
           def get_ten(self):          # ĐỪNG
               return self._ten
           def set_ten(self, ten):     # ĐỪNG
               self._ten = ten

       n.set_ten("Minh")
       print(n.get_ten())

   Python có cách gọn hơn nhiều, viết được:

       n.ten = "Minh"
       print(n.ten)

   mà vẫn kiểm tra được giá trị. Đó là @property — file 09 tiếp theo.

   Quy tắc Python: để attribute CÔNG KHAI nếu không cần kiểm tra gì.
   Chỉ khi cần kiểm tra mới chuyển sang @property. Đừng bọc getter/setter
   quanh mọi attribute "cho chắc" — đó là code rác.""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_08_encapsulation.py
#
# 1. class TheHocSinh: _diem là dict môn → điểm.
#    - them_diem(mon, diem) chặn điểm ngoài 0-10
#    - diem_tb() trả về trung bình
#    - xem_diem() trả về BẢN COPY của dict
# 2. class MatKhauLuuTru: không cho đọc lại mật khẩu, chỉ có kiem_tra(chuoi)
#    trả về True/False
# 3. Cho class TaiKhoanHo ở mục 2, viết 3 cách phá nó bằng cách gán trực tiếp
# 4. Tự trả lời: nếu Python không chặn được _attribute, thì dấu _ có ích gì?
