"""
TUẦN 1 — HÀM (phần quan trọng nhất của chặng A)

Vì sao hàm quan trọng với OOP?

    method chỉ là một hàm được gắn vào dữ liệu.

Hiểu hàm tốt thì tuần 3 (class) sẽ rất nhẹ. Hiểu hàm lỏng thì tuần 3 sẽ
thành học thuộc cú pháp mà không biết mình đang làm gì.

Chạy: python 02_ham.py
"""

# ---------------------------------------------------------------
# 1. HÀM CƠ BẢN
# ---------------------------------------------------------------
print("1. HÀM CƠ BẢN")


def chao(ten):
    """Hàm có 1 tham số, trả về một chuỗi."""
    return f"Xin chào, {ten}!"


print("  ", chao("Minh"))

# Hàm KHÔNG có return thì trả về None. Đây là lỗi hay gặp:
def in_chao(ten):
    print(f"   Xin chào, {ten}!")       # chỉ IN, không TRẢ VỀ


ket_qua = in_chao("Lan")
print(f"   in_chao trả về: {ket_qua}   ← None, vì hàm không có return")

# Phân biệt: print() đưa chữ ra màn hình. return đưa giá trị về cho người gọi.
# Người mới rất hay nhầm hai thứ này.


# ---------------------------------------------------------------
# 2. NHIỀU THAM SỐ, THAM SỐ MẶC ĐỊNH
# ---------------------------------------------------------------
print("\n2. THAM SỐ")


def tinh_tien(gia, so_luong, giam_gia=0.0):
    """giam_gia có giá trị mặc định → gọi hàm không cần truyền cũng được."""
    tong = gia * so_luong
    return tong * (1 - giam_gia)


print(f"   không giảm giá: {tinh_tien(100, 3):,.0f}")
print(f"   giảm 10%:       {tinh_tien(100, 3, 0.1):,.0f}")

# Gọi bằng TÊN tham số (keyword argument) — rõ ràng hơn nhiều khi hàm có
# nhiều tham số. Nên dùng.
print(f"   gọi bằng tên:   {tinh_tien(gia=100, so_luong=3, giam_gia=0.2):,.0f}")


# ---------------------------------------------------------------
# 3. SCOPE — PHẠM VI BIẾN
# ---------------------------------------------------------------
print("\n3. SCOPE")

tong_toan_cuc = 0       # biến toàn cục (global)


def cong_sai():
    tong_toan_cuc = 100      # tạo biến LOCAL MỚI, không sửa biến global
    return tong_toan_cuc


def cong_dung():
    global tong_toan_cuc     # nói rõ: tôi muốn sửa biến global
    tong_toan_cuc = 100


cong_sai()
print(f"   sau cong_sai():  tong_toan_cuc = {tong_toan_cuc}   ← không đổi")
cong_dung()
print(f"   sau cong_dung(): tong_toan_cuc = {tong_toan_cuc}  ← đã đổi")

# Thực tế: `global` hầu như không nên dùng. Nó làm code khó lần theo.
# OOP tồn tại một phần để giải quyết chính vấn đề này: thay vì dùng biến
# toàn cục, ta cho dữ liệu "thuộc về" một object.


# ---------------------------------------------------------------
# 4. MUTABLE vs IMMUTABLE — phần hay gây lỗi khó hiểu nhất
# ---------------------------------------------------------------
print("\n4. MUTABLE vs IMMUTABLE")

# int, float, str, tuple  → IMMUTABLE (không sửa được tại chỗ)
# list, dict, set         → MUTABLE   (sửa được tại chỗ)


def thu_doi_so(x):
    x = x + 1           # tạo giá trị mới, biến bên ngoài không đổi
    return x


def thu_doi_list(ds):
    ds.append(99)       # SỬA TẠI CHỖ → biến bên ngoài ĐỔI THEO


so = 10
thu_doi_so(so)
print(f"   số sau khi gọi hàm:  {so}          ← không đổi (immutable)")

danh_sach = [1, 2, 3]
thu_doi_list(danh_sach)
print(f"   list sau khi gọi hàm: {danh_sach}  ← ĐÃ ĐỔI (mutable)")

# Vì sao? Vì truyền vào hàm là truyền THAM CHIẾU tới cùng một object.
# id() cho thấy hai tên cùng trỏ vào một object:
a = [1, 2, 3]
b = a                    # KHÔNG copy — b và a là cùng một list
b.append(4)
print(f"   a = {a}, b = {b}   ← a đổi theo, vì a và b là cùng một object")
print(f"   id(a) == id(b): {id(a) == id(b)}")

# Muốn copy thật:
c = a.copy()             # hoặc list(a) / a[:]
c.append(5)
print(f"   sau khi copy: a = {a}, c = {c}   ← giờ đã độc lập")

# ĐÂY LÀ NGUỒN GỐC phần lớn lỗi "sao object của tôi tự đổi?" ở tuần 3.


# ---------------------------------------------------------------
# 5. BẪY: THAM SỐ MẶC ĐỊNH LÀ MUTABLE
# ---------------------------------------------------------------
print("\n5. BẪY NỔI TIẾNG")


def them_sai(mon, danh_sach=[]):          # ❌ ĐỪNG BAO GIỜ VIẾT THẾ NÀY
    danh_sach.append(mon)
    return danh_sach


print(f"   lần 1: {them_sai('Toán')}")
print(f"   lần 2: {them_sai('Lý')}      ← còn nguyên 'Toán'! ")
print(f"   lần 3: {them_sai('Hóa')}   ← list mặc định bị dùng chung")

# Vì sao: list mặc định được tạo MỘT LẦN lúc định nghĩa hàm, không phải
# mỗi lần gọi. Cách viết đúng:


def them_dung(mon, danh_sach=None):      # ✅
    if danh_sach is None:
        danh_sach = []
    danh_sach.append(mon)
    return danh_sach


print(f"   đúng lần 1: {them_dung('Toán')}")
print(f"   đúng lần 2: {them_dung('Lý')}")

# Bẫy này sẽ quay lại ở tuần 3 với __init__(self, items=[]). Nhớ nó.


# ---------------------------------------------------------------
# 6. TÁCH BÀI TOÁN LỚN THÀNH HÀM NHỎ
# ---------------------------------------------------------------
print("\n6. TÁCH HÀM")

# Đây là kỹ năng cốt lõi. OOP chỉ là bước tiếp theo của việc này.


def doc_diem(diem_cac_mon):
    return sum(diem_cac_mon) / len(diem_cac_mon)


def xep_loai(diem_tb):
    if diem_tb >= 8.5:
        return "Giỏi"
    if diem_tb >= 7.0:
        return "Khá"
    if diem_tb >= 5.0:
        return "Trung bình"
    return "Yếu"


def bao_cao(ten, diem_cac_mon):
    tb = doc_diem(diem_cac_mon)
    return f"{ten}: TB {tb:.2f} — {xep_loai(tb)}"


print("  ", bao_cao("Minh", [9, 8, 8.5]))
print("  ", bao_cao("Lan", [6, 5.5, 7]))

# Mỗi hàm làm MỘT việc, tên hàm nói rõ nó làm gì. Khi đọc bao_cao() bạn
# hiểu ngay logic mà không cần đọc chi tiết hai hàm kia.


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_02_ham.py
#
# 1. Viết hàm tinh_bmi(cao_m, nang_kg) trả về BMI = nang / cao²
# 2. Viết hàm phan_loai_bmi(bmi): < 18.5 "Gầy", 18.5-24.9 "Bình thường",
#    25-29.9 "Thừa cân", >= 30 "Béo phì"
# 3. Viết hàm dao_nguoc(s) trả về chuỗi đảo ngược, KHÔNG dùng s[::-1]
# 4. Viết hàm them_an_toan(phan_tu, ds=None) không mắc bẫy mục 5
# 5. Trả lời bằng lời (viết trong comment): vì sao sửa list trong hàm
#    thì list bên ngoài cũng đổi, còn sửa số thì không?
