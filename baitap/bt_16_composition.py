"""
BÀI TẬP — 06-composition/16_composition_vs_inheritance.py
Chạy: python bt_16_composition.py
"""


# --- BÀI 1 ------------------------------------------------------
class CPU:
    """__init__(ten, so_nhan). mo_ta() -> "i5 (4 nhân)" """
    # TODO


class RAM:
    """__init__(gb). mo_ta() -> "8GB" """
    # TODO


class OCung:
    """__init__(gb, loai). mo_ta() -> "512GB SSD" """
    # TODO


class MayTinh:
    """__init__(ten, cpu, ram, o_cung) — COMPOSITION, không kế thừa.
    nang_cap_ram(ram_moi) đổi RAM, trả chuỗi "8GB -> 16GB"
    thong_tin() -> "Dell: i5 (4 nhân), 8GB, 512GB SSD" """
    # TODO


# --- BÀI 2: chọn kế thừa hay composition ------------------------
# Với mỗi cặp, ghi "ke_thua" hoặc "composition" và GIẢI THÍCH một dòng.
CAU_TRA_LOI = {
    "NguoiDung / TaiKhoanAdmin": "TODO",
    "DonHang / DiaChiGiaoHang": "TODO",
    "Hinh / HinhTron": "TODO",
    "NhaHang / ThucDon": "TODO",
    "Logger / LoggerGhiFile": "TODO",
    "GioHang / MaGiamGia": "TODO",
}
GIAI_THICH = {
    # "NguoiDung / TaiKhoanAdmin": "admin LÀ MỘT người dùng, quan hệ bất biến",
    # TODO: viết giải thích cho cả 6 cặp
}


# --- BÀI 3: Strategy bằng composition --------------------------
class TinhDiemThuong:
    """tinh(diem_goc, giay_da_choi) -> diem_goc"""
    # TODO


class TinhDiemNhanDoi:
    """tinh(...) -> diem_goc * 2"""
    # TODO


class TinhDiemTheoThoiGian:
    """tinh(diem_goc, giay) -> diem_goc + max(0, 60 - giay) * 10
    (xong nhanh thì được thêm điểm)"""
    # TODO


class TroChoi:
    """__init__(ten, cach_tinh=None) — mặc định TinhDiemThuong
    doi_cach_tinh(moi)
    ket_thuc(diem_goc, giay) -> điểm cuối cùng theo cách tính hiện tại"""
    # TODO


# --- BÀI 4: viết lại bài kế thừa bằng composition --------------
# Lấy class TaiKhoanThanhToan ở bt_10 (kế thừa TaiKhoan, rút có phí).
# Viết lại bằng composition: TaiKhoan CÓ một "chính sách phí".
class PhiCoDinh:
    """__init__(phi). tinh(so_tien) -> phi"""
    # TODO


class PhiPhanTram:
    """__init__(ty_le). tinh(so_tien) -> so_tien * ty_le"""
    # TODO


class KhongPhi:
    """tinh(so_tien) -> 0"""
    # TODO


class TaiKhoan:
    """__init__(chu, so_du=0, chinh_sach_phi=None) — mặc định KhongPhi
    rut(tien) trừ tien + phí, raise ValueError nếu không đủ
    doi_chinh_sach(moi) — việc kế thừa KHÔNG làm được"""
    # TODO


# Cách nào dễ thêm tính năng mới hơn? TRẢ LỜI: TODO


# ===============================================================
# TỰ KIỂM
# ===============================================================
if __name__ == "__main__":
    mt = MayTinh("Dell", CPU("i5", 4), RAM(8), OCung(512, "SSD"))
    assert mt.thong_tin() == "Dell: i5 (4 nhân), 8GB, 512GB SSD", \
        f"bài 1: nhận {mt.thong_tin()!r}"
    assert mt.nang_cap_ram(RAM(16)) == "8GB -> 16GB", "bài 1"
    assert "16GB" in mt.thong_tin(), "bài 1: nâng cấp phải có hiệu lực"
    assert MayTinh.__bases__ == (object,), "bài 1: MayTinh không kế thừa gì"

    for cap, dap in CAU_TRA_LOI.items():
        assert dap in ("ke_thua", "composition"), f"bài 2: chưa trả lời {cap!r}"
    assert len(GIAI_THICH) == 6, "bài 2: cần giải thích cho cả 6 cặp"

    g = TroChoi("Xếp hình")
    assert g.ket_thuc(100, 90) == 100, "bài 3: mặc định là điểm thường"
    g.doi_cach_tinh(TinhDiemNhanDoi())
    assert g.ket_thuc(100, 90) == 200, "bài 3: nhân đôi"
    g.doi_cach_tinh(TinhDiemTheoThoiGian())
    assert g.ket_thuc(100, 30) == 400, f"bài 3: nhận {g.ket_thuc(100, 30)}"
    assert g.ket_thuc(100, 90) == 100, "bài 3: quá 60 giây thì không thưởng"

    t = TaiKhoan("Minh", 100_000)
    t.rut(50_000)
    assert t.so_du == 50_000, f"bài 4: không phí, nhận {t.so_du}"

    t2 = TaiKhoan("Lan", 100_000, PhiCoDinh(5_000))
    t2.rut(50_000)
    assert t2.so_du == 45_000, f"bài 4: nhận {t2.so_du}"

    t2.doi_chinh_sach(PhiPhanTram(0.1))
    t2.rut(10_000)
    assert t2.so_du == 34_000, f"bài 4: phí 10% của 10k = 1k, nhận {t2.so_du}"

    t3 = TaiKhoan("Hùng", 10_000, PhiCoDinh(5_000))
    try:
        t3.rut(10_000)
        raise AssertionError("bài 4: phải chặn vì 10k + 5k phí > 10k")
    except ValueError:
        pass

    print("TẤT CẢ BÀI TẬP ĐÚNG")
