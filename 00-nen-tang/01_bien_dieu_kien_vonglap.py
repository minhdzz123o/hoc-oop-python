"""
TUẦN 1 — Cú pháp tối thiểu

Đây là phần duy nhất bạn cần học thuộc. Phần còn lại của lộ trình là cách
TỔ CHỨC những thứ này cho gọn khi chương trình lớn lên.

Chạy: python 01_bien_dieu_kien_vonglap.py
"""

# ---------------------------------------------------------------
# 1. BIẾN VÀ KIỂU DỮ LIỆU
# ---------------------------------------------------------------
# Python không cần khai báo kiểu. Kiểu được suy ra từ giá trị.

ten = "Minh"          # str   — chuỗi
tuoi = 20             # int   — số nguyên
diem = 8.5            # float — số thực
dang_hoc = True       # bool  — True / False

print("1. BIẾN VÀ KIỂU")
print(f"   {ten}, {tuoi} tuổi, điểm {diem}, đang học: {dang_hoc}")

# type() cho biết kiểu của một giá trị. Dùng nhiều khi debug.
print(f"   kiểu của tuoi là {type(tuoi).__name__}, của diem là {type(diem).__name__}")

# Chú ý: phép chia / luôn ra float, kể cả khi chia hết
print(f"   10 / 2 = {10 / 2}   (float, không phải 5)")
print(f"   10 // 2 = {10 // 2}  (// là chia lấy nguyên)")
print(f"   10 % 3 = {10 % 3}   (% là chia lấy dư)")


# ---------------------------------------------------------------
# 2. IF / ELIF / ELSE
# ---------------------------------------------------------------
# Python dùng THỤT LỀ (indent) để xác định khối lệnh, không dùng { }.
# Thụt lề sai = chương trình sai. Luôn dùng 4 dấu cách.

print("\n2. ĐIỀU KIỆN")

if diem >= 8.5:
    xep_loai = "Giỏi"
elif diem >= 7.0:
    xep_loai = "Khá"
elif diem >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

print(f"   điểm {diem} → {xep_loai}")

# Toán tử logic: and, or, not  (không phải &&, ||, !)
if tuoi >= 18 and dang_hoc:
    print("   sinh viên đủ 18 tuổi")


# ---------------------------------------------------------------
# 3. VÒNG LẶP FOR
# ---------------------------------------------------------------
print("\n3. VÒNG LẶP FOR")

# range(5) sinh ra 0,1,2,3,4 — KHÔNG có 5. Đây là lỗi kinh điển của người mới.
print("   range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(bắt_đầu, kết_thúc, bước)
print("   range(2, 11, 2):", end=" ")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Lặp trực tiếp qua các phần tử — cách Pythonic, dùng cái này thay vì range(len(...))
mon_hoc = ["Toán", "Lý", "Hóa"]
print("   lặp qua list:", end=" ")
for mon in mon_hoc:
    print(mon, end=" ")
print()

# Cần cả chỉ số và giá trị thì dùng enumerate
print("   với enumerate:")
for chi_so, mon in enumerate(mon_hoc, start=1):
    print(f"      {chi_so}. {mon}")


# ---------------------------------------------------------------
# 4. VÒNG LẶP WHILE
# ---------------------------------------------------------------
# Dùng khi chưa biết trước số lần lặp.
print("\n4. VÒNG LẶP WHILE")

so_du = 100
lan = 0
while so_du >= 30:
    so_du -= 30
    lan += 1
print(f"   rút 30 được {lan} lần, còn lại {so_du}")

# BẪY: nếu quên thay đổi biến điều kiện bên trong while → lặp vô hạn.
# Mỗi lần viết while, hãy tự hỏi: "biến nào sẽ làm điều kiện thành False?"


# ---------------------------------------------------------------
# 5. BREAK VÀ CONTINUE
# ---------------------------------------------------------------
print("\n5. BREAK / CONTINUE")

print("   bỏ qua số chẵn, dừng khi gặp 7:", end=" ")
for i in range(1, 20):
    if i % 2 == 0:
        continue      # bỏ qua phần còn lại, sang vòng lặp kế
    if i == 7:
        break         # thoát hẳn vòng lặp
    print(i, end=" ")
print()


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_01_co_ban.py
#
# 1. In bảng cửu chương của 7 (từ 7x1 đến 7x10)
# 2. Tính tổng các số từ 1 đến 100 chia hết cho 3
# 3. Cho tuổi, in ra: dưới 13 "Trẻ em", 13-19 "Thiếu niên",
#    20-59 "Người trưởng thành", từ 60 "Người cao tuổi"
# 4. Đếm xem số 1234567 có bao nhiêu chữ số (dùng while và //)
