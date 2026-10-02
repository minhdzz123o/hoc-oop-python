"""
TUẦN 2 — LIST VÀ DICT

Hai cấu trúc này bạn sẽ dùng suốt. Ở tuần 3, list sẽ chứa các object,
còn dict là tiền đề trực tiếp của class.

Chạy: python 03_list_dict.py
"""

# ---------------------------------------------------------------
# 1. LIST
# ---------------------------------------------------------------
print("1. LIST")

mon = ["Toán", "Lý", "Hóa"]

print(f"   mon          = {mon}")
print(f"   mon[0]       = {mon[0]}        ← đếm từ 0")
print(f"   mon[-1]      = {mon[-1]}        ← phần tử cuối")
print(f"   mon[0:2]     = {mon[0:2]}   ← lấy từ 0 đến TRƯỚC 2")
print(f"   len(mon)     = {len(mon)}")

mon.append("Sinh")           # thêm vào cuối
mon.insert(0, "Văn")         # chèn vào vị trí
mon.remove("Lý")             # xóa theo giá trị
print(f"   sau sửa đổi  = {mon}")

print(f"   'Toán' in mon: {'Toán' in mon}   ← kiểm tra tồn tại")

# Sắp xếp
diem = [7, 9, 5, 8]
print(f"   sorted(diem)             = {sorted(diem)}      ← trả list MỚI")
print(f"   sorted(diem, reverse=True) = {sorted(diem, reverse=True)}")
diem.sort()                  # sửa TẠI CHỖ, trả về None
print(f"   sau diem.sort()          = {diem}")

# BẪY: x = diem.sort() sẽ cho x = None. Nhớ phân biệt sort() và sorted().


# ---------------------------------------------------------------
# 2. LIST COMPREHENSION
# ---------------------------------------------------------------
print("\n2. LIST COMPREHENSION")

# Cách dài:
binh_phuong = []
for i in range(1, 6):
    binh_phuong.append(i * i)

# Cách Pythonic — cùng kết quả, một dòng:
binh_phuong_2 = [i * i for i in range(1, 6)]

print(f"   [i*i for i in range(1,6)]           = {binh_phuong_2}")
print(f"   có điều kiện: {[i for i in range(1, 21) if i % 3 == 0]}")

# Dùng được với bất cứ thứ gì lặp được:
diem_cac_mon = [7.5, 9.0, 4.5, 8.0]
print(f"   môn đạt (>=5): {[d for d in diem_cac_mon if d >= 5]}")

# Hàm tiện ích hay dùng:
print(f"   sum  = {sum(diem_cac_mon)}")
print(f"   max  = {max(diem_cac_mon)}, min = {min(diem_cac_mon)}")
print(f"   TB   = {sum(diem_cac_mon) / len(diem_cac_mon):.2f}")


# ---------------------------------------------------------------
# 3. DICT — cặp khóa: giá trị
# ---------------------------------------------------------------
print("\n3. DICT")

sinh_vien = {
    "ten": "Minh",
    "tuoi": 20,
    "diem": [9, 8, 8.5],
}

print(f"   sinh_vien['ten']  = {sinh_vien['ten']}")
print(f"   các khóa          = {list(sinh_vien.keys())}")
print(f"   các giá trị       = {list(sinh_vien.values())}")

# Thêm / sửa khóa — cùng một cú pháp
sinh_vien["lop"] = "K20"
sinh_vien["tuoi"] = 21
print(f"   sau khi thêm 'lop': {list(sinh_vien.keys())}")

# Truy cập khóa không tồn tại → KeyError (crash).
# Dùng .get() để có giá trị mặc định thay vì crash:
print(f"   sinh_vien.get('sdt')           = {sinh_vien.get('sdt')}      ← None")
print(f"   sinh_vien.get('sdt', 'chưa có') = {sinh_vien.get('sdt', 'chưa có')}")

# Lặp qua dict:
print("   lặp qua dict:")
for khoa, gia_tri in sinh_vien.items():
    print(f"      {khoa}: {gia_tri}")


# ---------------------------------------------------------------
# 4. LIST CỦA DICT — cách tổ chức dữ liệu phổ biến nhất khi chưa có class
# ---------------------------------------------------------------
print("\n4. LIST CỦA DICT")

lop = [
    {"ten": "Minh", "diem": 8.5},
    {"ten": "Lan", "diem": 6.0},
    {"ten": "Hùng", "diem": 9.2},
]

for sv in lop:
    print(f"   {sv['ten']:6} {sv['diem']}")

# Sắp xếp theo điểm — key nhận một hàm nói "sắp theo cái gì"
theo_diem = sorted(lop, key=lambda sv: sv["diem"], reverse=True)
print(f"   cao điểm nhất: {theo_diem[0]['ten']}")

diem_tb_lop = sum(sv["diem"] for sv in lop) / len(lop)
print(f"   TB lớp: {diem_tb_lop:.2f}")


# ---------------------------------------------------------------
# 5. TUPLE VÀ SET (biết là đủ, dùng ít hơn)
# ---------------------------------------------------------------
print("\n5. TUPLE VÀ SET")

toa_do = (10, 20)            # tuple — như list nhưng KHÔNG sửa được
print(f"   tuple: {toa_do}, x = {toa_do[0]}")

x, y = toa_do                # unpacking — rất hay dùng
print(f"   unpacking: x={x}, y={y}")

ngon_ngu = {"Python", "Java", "Python", "C++"}   # set — không trùng lặp
print(f"   set tự loại trùng: {sorted(ngon_ngu)}")


# ===============================================================
# === BÀI TẬP ===
# ===============================================================
# Làm trong file baitap/bt_03_list_dict.py
#
# 1. Cho list số, trả về list chỉ chứa số chẵn (dùng comprehension)
# 2. Đếm số lần xuất hiện của mỗi chữ cái trong một chuỗi, trả về dict
# 3. Cho list[dict] sinh viên, viết hàm:
#    - them_sv(lop, ten, diem)
#    - tim_sv(lop, ten)        → trả về dict hoặc None
#    - diem_cao_nhat(lop)      → trả về tên
# 4. Gộp hai dict thành một (khóa trùng thì lấy giá trị của dict thứ hai)
