"""
TUẦN 2 — FILE QUAN TRỌNG NHẤT CHẶNG A

Mục tiêu của file này KHÔNG phải dạy cú pháp mới.
Mục tiêu là làm bạn tự thấy: cách làm hiện tại có vấn đề gì.

Nếu bạn đọc file này mà thấy "đúng rồi, bất tiện thật" thì tuần 3 sẽ rất nhẹ.

Chạy: python 04_dict_lam_doi_tuong.py
"""

# ===============================================================
# CÁCH LÀM HIỆN TẠI: dict chứa dữ liệu + hàm xử lý riêng
# ===============================================================

print("=" * 60)
print("CÁCH LÀM VỚI DICT")
print("=" * 60)


def tao_tai_khoan(chu_so_huu, so_du=0):
    return {"chu_so_huu": chu_so_huu, "so_du": so_du, "lich_su": []}


def nap(tk, tien):
    if tien <= 0:
        raise ValueError("Số tiền nạp phải dương")
    tk["so_du"] += tien
    tk["lich_su"].append(f"nạp {tien}")


def rut(tk, tien):
    if tien <= 0:
        raise ValueError("Số tiền rút phải dương")
    if tien > tk["so_du"]:
        raise ValueError("Không đủ số dư")
    tk["so_du"] -= tien
    tk["lich_su"].append(f"rút {tien}")


tk = tao_tai_khoan("Minh", 1000)
nap(tk, 500)
rut(tk, 200)
print(f"\nTài khoản của {tk['chu_so_huu']}: {tk['so_du']}")
print(f"Lịch sử: {tk['lich_su']}")

# Hoạt động được. Nhưng có 4 vấn đề.


# ===============================================================
# VẤN ĐỀ 1 — Không ai bảo vệ được dữ liệu
# ===============================================================
print("\n" + "=" * 60)
print("VẤN ĐỀ 1: dữ liệu không được bảo vệ")
print("=" * 60)

tk["so_du"] = 999_999_999        # không qua kiểm tra nào cả!
print(f"\nGán trực tiếp so_du: {tk['so_du']}")
print("→ Mọi công sức kiểm tra trong nap()/rut() thành vô nghĩa.")
print("→ Và lịch_su không ghi gì, nên không ai biết chuyện gì đã xảy ra.")

tk["so_du"] = -5000              # số dư âm, vô lý
print(f"Gán số âm:           {tk['so_du']}   ← trạng thái không hợp lệ")


# ===============================================================
# VẤN ĐỀ 2 — Gõ sai tên khóa, Python không hề báo
# ===============================================================
print("\n" + "=" * 60)
print("VẤN ĐỀ 2: gõ sai khóa không bị phát hiện")
print("=" * 60)

tk2 = tao_tai_khoan("Lan", 1000)
tk2["sodu"] = 5000               # thiếu dấu gạch dưới → tạo khóa MỚI

print(f"\nso_du thật:  {tk2['so_du']}")
print(f"khóa bị gõ sai: {tk2['sodu']}")
print(f"các khóa hiện có: {list(tk2.keys())}")
print("→ Không có lỗi nào. Bug này nằm im tới khi khách hàng phàn nàn.")


# ===============================================================
# VẤN ĐỀ 3 — Hàm và dữ liệu rời nhau
# ===============================================================
print("\n" + "=" * 60)
print("VẤN ĐỀ 3: hàm và dữ liệu không đi cùng nhau")
print("=" * 60)

print("""
Nhìn vào `tk` bạn KHÔNG biết được những hàm nào dùng được với nó.
Phải tự nhớ: nap, rut, tao_tai_khoan... Chúng chỉ liên quan với nhau
bằng trí nhớ của người viết, không có gì trong code nói lên điều đó.

Khi thêm loại tài khoản mới (tiết kiệm, tín dụng) bạn phải viết:
    nap_tiet_kiem(tk, tien)
    rut_tiet_kiem(tk, tien)
    nap_tin_dung(tk, tien)
    ...
và mỗi lần dùng lại phải tự nhớ gọi đúng hàm cho đúng loại dict.
""")


# ===============================================================
# VẤN ĐỀ 4 — Mọi hàm phải truyền `tk` thủ công
# ===============================================================
print("=" * 60)
print("VẤN ĐỀ 4: lặp lại tham số")
print("=" * 60)

print("""
    nap(tk, 500)
    rut(tk, 200)
    xem_lich_su(tk)
    tinh_lai(tk)

`tk` xuất hiện ở mọi lời gọi. Nếu có 20 hàm thì lặp 20 lần.
""")


# ===============================================================
# ĐIỀU BẠN CẦN GHI NHỚ
# ===============================================================
print("=" * 60)
print("TUẦN 3 SẼ GIẢI QUYẾT GÌ")
print("=" * 60)

print("""
Cả 4 vấn đề trên có CÙNG MỘT gốc:

    dữ liệu và các hành vi xử lý nó bị để rời nhau.

Tuần 3 ta gộp chúng vào một chỗ — gọi là CLASS. Nhìn trước cho quen mắt:

    class TaiKhoan:
        def __init__(self, chu_so_huu, so_du=0):
            self.chu_so_huu = chu_so_huu
            self._so_du = so_du          # dấu _ : đừng chạm từ ngoài
            self._lich_su = []

        def nap(self, tien):             # hàm nằm NGAY TRONG class
            if tien <= 0:
                raise ValueError("Số tiền nạp phải dương")
            self._so_du += tien

    tk = TaiKhoan("Minh", 1000)
    tk.nap(500)                          # không phải nap(tk, 500)
    print(tk.so_du)

So sánh:

  dict                        class
  ----------------------      -------------------------------
  tao_tai_khoan("Minh")       TaiKhoan("Minh")
  nap(tk, 500)                tk.nap(500)
  tk["so_du"]                 tk.so_du
  tk["so_du"] = -5000  (!)    bị chặn bởi @property (tuần 4)
  tk["sodu"] gõ sai, im lặng  tk.sodu → AttributeError ngay

OOP không phải phép màu. Nó chỉ là: ĐẶT DỮ LIỆU VÀ HÀNH VI CẠNH NHAU,
rồi kiểm soát ai được chạm vào cái gì.

Mỗi khi học một khái niệm OOP mới, hãy tự hỏi:
"nó giải quyết vấn đề gì mà cách cũ không làm được?"
""")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_04_cau_noi.py
#
# 1. Dùng dict + hàm, viết một "giỏ hàng":
#       tao_gio() / them_mon(gio, ten, gia, sl) / tong_tien(gio)
# 2. Chỉ ra ít nhất 2 cách người dùng code của bạn có thể làm hỏng
#    giỏ hàng bằng cách gán trực tiếp vào dict
# 3. Viết trong comment: nếu được "cấm" người ta chạm vào một khóa
#    trong dict, bạn sẽ cấm khóa nào, vì sao?
#
# ĐỪNG viết class ở bài này. Mục đích là cảm nhận cái bất tiện trước.
