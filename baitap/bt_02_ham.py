"""
BÀI TẬP — 00-nen-tang/02_ham.py
Chạy: python bt_02_ham.py
"""


# --- BÀI 1 ------------------------------------------------------
def tinh_bmi(cao_m, nang_kg):
    """BMI = nang / cao^2. Làm tròn 1 chữ số thập phân."""
    # TODO
    return 0.0


# --- BÀI 2 ------------------------------------------------------
def phan_loai_bmi(bmi):
    """< 18.5 "Gầy" | 18.5-24.9 "Bình thường" | 25-29.9 "Thừa cân"
    | >= 30 "Béo phì" """
    # TODO
    return ""


# --- BÀI 3 ------------------------------------------------------
def dao_nguoc(s):
    """Đảo ngược chuỗi. KHÔNG dùng s[::-1] và KHÔNG dùng reversed()."""
    # TODO
    return ""


# --- BÀI 4 ------------------------------------------------------
def them_an_toan(phan_tu, ds=None):
    """Thêm phan_tu vào ds và trả về ds.
    Gọi không truyền ds thì mỗi lần phải được một list MỚI.
    (tránh bẫy mutable default argument)"""
    # TODO
    return []


# --- BÀI 5: trả lời bằng lời -----------------------------------
# Vì sao sửa list trong hàm thì list bên ngoài cũng đổi, còn sửa số thì không?
#
# TRẢ LỜI:
# TODO viết câu trả lời của bạn ở đây


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    assert tinh_bmi(1.70, 65) == 22.5, f"bài 1: nhận {tinh_bmi(1.70, 65)}"
    assert tinh_bmi(1.80, 90) == 27.8, f"bài 1: nhận {tinh_bmi(1.80, 90)}"

    for bmi, mong in [(17.0, "Gầy"), (18.5, "Bình thường"), (24.9, "Bình thường"),
                      (25.0, "Thừa cân"), (29.9, "Thừa cân"), (30.0, "Béo phì")]:
        got = phan_loai_bmi(bmi)
        assert got == mong, f"bài 2: BMI {bmi} → cần {mong!r}, nhận {got!r}"

    assert dao_nguoc("Python") == "nohtyP", f"bài 3: nhận {dao_nguoc('Python')!r}"
    assert dao_nguoc("") == "", "bài 3: chuỗi rỗng"
    assert dao_nguoc("a") == "a", "bài 3: một ký tự"

    assert them_an_toan("a") == ["a"], "bài 4: lần gọi đầu"
    assert them_an_toan("b") == ["b"], "bài 4: MẮC BẪY mutable default!"
    assert them_an_toan("c", ["x"]) == ["x", "c"], "bài 4: truyền ds sẵn có"

    print("TẤT CẢ BÀI TẬP ĐÚNG")
