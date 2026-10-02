"""
TUẦN 6 — DUCK TYPING: ĐA HÌNH KIỂU PYTHON

"If it walks like a duck and quacks like a duck, it's a duck."

Trong Java, muốn đa hình thì các class PHẢI cùng kế thừa một lớp cha
hoặc cùng implement một interface.

Trong Python: KHÔNG CẦN. Chỉ cần có method cùng tên là xong.

Đây là điểm khác biệt lớn nhất giữa OOP Python và OOP Java. Nếu bạn học
OOP từ tài liệu Java rồi viết Python, phần này sẽ làm bạn nhẹ đi rất nhiều.

Chạy: python 13_duck_typing.py
"""

# ---------------------------------------------------------------
# 1. ĐA HÌNH KHÔNG CẦN KẾ THỪA
# ---------------------------------------------------------------
print("1. KHÔNG KẾ THỪA GÌ CẢ")


class Vit:
    def keu(self):
        return "cạc cạc"


class Nguoi:                       # không kế thừa Vit
    def keu(self):
        return "tôi đang giả tiếng vịt"


class Robot:                       # cũng không
    def keu(self):
        return "beep cạc beep"


# Hàm này không quan tâm bạn là gì, chỉ cần bạn có method keu()
def cho_keu(ai):
    return ai.keu()


for x in [Vit(), Nguoi(), Robot()]:
    print(f"   {type(x).__name__:8} → {cho_keu(x)}")

print("""
   Ba class hoàn toàn không liên quan huyết thống. Vẫn dùng thay nhau được.
   Trong Java bạn sẽ phải tạo interface Quackable và cho cả ba implement nó.""")


# ---------------------------------------------------------------
# 2. VÌ SAO ĐIỀU NÀY HỮU ÍCH — TEST CODE
# ---------------------------------------------------------------
print("2. ỨNG DỤNG: THAY THẾ ĐỂ TEST")


class EmailThat:
    def gui(self, den, noi_dung):
        # trong thực tế: kết nối SMTP, tốn thời gian, tốn tiền
        return f"ĐÃ GỬI THẬT tới {den}"


class EmailGia:
    """Dùng khi test — không gửi gì, chỉ ghi lại."""

    def __init__(self):
        self.da_gui = []

    def gui(self, den, noi_dung):
        self.da_gui.append((den, noi_dung))
        return f"(giả) ghi nhận gửi tới {den}"


def thong_bao_don_hang(bo_gui, khach, ma_don):
    """Code nghiệp vụ — không biết và không cần biết bo_gui là loại nào."""
    return bo_gui.gui(khach, f"Đơn {ma_don} đã xác nhận")


print(f"   chạy thật: {thong_bao_don_hang(EmailThat(), 'minh@a.com', 'DH01')}")

gia = EmailGia()
print(f"   khi test:  {thong_bao_don_hang(gia, 'minh@a.com', 'DH01')}")
print(f"   kiểm tra:  đã gọi {len(gia.da_gui)} lần, tới {gia.da_gui[0][0]}")

print("""
   EmailGia không kế thừa EmailThat. Chúng chỉ TÌNH CỜ có cùng method gui().
   Nhờ vậy bạn test được code nghiệp vụ mà không gửi email thật.
   Trong thực tế đây là kỹ thuật "mock", dùng ở mọi dự án Python nghiêm túc.""")


# ---------------------------------------------------------------
# 3. ĐA HÌNH VỚI CHÍNH KIỂU DỮ LIỆU CÓ SẴN
# ---------------------------------------------------------------
print("3. PYTHON ĐÃ DÙNG ĐA HÌNH KHẮP NƠI")

# len() hoạt động với mọi thứ có __len__
for x in ["chuỗi", [1, 2, 3], {"a": 1}, (1, 2), {1, 2, 3, 4}]:
    print(f"   len({type(x).__name__:5}) = {len(x)}")

# + hoạt động khác nhau tùy kiểu — cũng là đa hình
print(f"\n   1 + 2        = {1 + 2}")
print(f"   'a' + 'b'    = {'a' + 'b'!r}")
print(f"   [1] + [2]    = {[1] + [2]}")

print("""
   Bạn đã dùng đa hình từ tuần 1 mà không biết. len(), +, for, in — tất cả
   đều gọi method tương ứng trên object, và mỗi kiểu tự cài đặt khác nhau.
   File 17 (tuần 8) sẽ cho bạn tự làm điều này với class của mình.""")


# ---------------------------------------------------------------
# 4. XIN THA LỖI DỄ HƠN XIN PHÉP (EAFP)
# ---------------------------------------------------------------
print("4. EAFP: CÁCH KIỂM TRA KIỂU PYTHONIC")


class Ca:
    def boi(self):
        return "đang bơi"


def xu_ly_kieu_java(con_vat):
    """Cách người học Java hay viết — kiểm tra kiểu trước."""
    if isinstance(con_vat, Vit):
        return con_vat.keu()
    elif isinstance(con_vat, Robot):
        return con_vat.keu()
    return "không biết xử lý"


def xu_ly_pythonic(con_vat):
    """Cách Pythonic — cứ gọi, xử lý khi không được."""
    try:
        return con_vat.keu()
    except AttributeError:
        return f"{type(con_vat).__name__} không biết kêu"


print(f"   kiểu Java với Nguoi():    {xu_ly_kieu_java(Nguoi())}")
print(f"   ← sai, vì phải thêm isinstance cho MỌI class mới")
print(f"   Pythonic với Nguoi():     {xu_ly_pythonic(Nguoi())}")
print(f"   Pythonic với Ca():        {xu_ly_pythonic(Ca())}")

print("""
   EAFP = Easier to Ask Forgiveness than Permission.
   Dùng try/except thay vì isinstance. Code tự động hoạt động với
   class mới mà không cần sửa.

   Khi nào vẫn nên dùng isinstance?
   - validate đầu vào ở biên hệ thống (file 09: isinstance(x, (int, float)))
   - khi thật sự cần xử lý khác nhau theo kiểu và không kiểm soát được class

   Phần lớn thời gian: đừng kiểm tra kiểu, cứ gọi method.""")


# ---------------------------------------------------------------
# 5. HẠN CHẾ CỦA DUCK TYPING
# ---------------------------------------------------------------
print("5. MẶT TRÁI")

print("""   Duck typing linh hoạt, nhưng:

   - Không có gì nói cho bạn biết một class CẦN có method nào.
     Gõ sai tên method → lỗi chỉ hiện ra lúc chạy, có thể rất muộn.
   - Đọc code khó hơn: hàm nhận tham số `bo_gui` — bo_gui cần có gì?
     Phải đọc hết thân hàm mới biết.

   Tuần 7 cho hai cách khắc phục mà vẫn giữ tinh thần Python:
     - abc.ABC          → BẮT BUỘC lớp con cài đặt method
     - typing.Protocol  → KHAI BÁO "cần có method gì" mà không cần kế thừa""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_13_duck_typing.py
#
# 1. Viết 3 class KHÔNG kế thừa nhau: GhiFile, GhiManHinh, GhiBoNho,
#    mỗi cái có ghi(dong). Viết hàm ghi_log(bo_ghi, cac_dong) dùng được cả ba.
# 2. Viết LuuTruGia (dict trong RAM) có cùng method lay(khoa)/dat(khoa, gia_tri)
#    như một LuuTruFile (ghi ra file json). Dùng cái giả để test một hàm
#    dem_truy_cap(luu_tru) mà không tạo file nào.
# 3. Viết hàm tong_an_toan(cac_thu) cộng mọi phần tử, bỏ qua phần tử
#    không cộng được (dùng try/except, không dùng isinstance)
# 4. Tự trả lời: duck typing có ưu điểm gì so với interface của Java,
#    và nhược điểm gì?
