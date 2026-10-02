# Dự án 1 — Quản lý thư viện

Làm sau khi xong tuần 7. Dự án này dùng: encapsulation, inheritance,
polymorphism, abstract class, composition.

## Chạy

```bash
python main.py
```

Lúc đầu sẽ báo lỗi ở các `TODO` — đó là phần bạn viết.
Khi xong, `main.py` chạy trọn một kịch bản mượn/trả và in báo cáo.

## Yêu cầu chức năng

### Tài liệu
- `TaiLieu` là **abstract class** (`abc.ABC`) với:
  - `@abstractmethod so_ngay_muon()` — mỗi loại có hạn khác nhau
  - `@abstractmethod loai()` — tên loại để in ra
  - method **dùng chung**: `cho_muon()`, `tra()`, `phi_tre(so_ngay)`, `mo_ta()`
- Ba lớp con: `Sach` (30 ngày), `Bao` (3 ngày, phí trễ gấp 4), `DiaDVD` (7 ngày)

### Thành viên
- `ThanhVien` với `_dang_muon` được **đóng gói** — chỉ đổi được qua method
- `ThanhVienThuong` mượn tối đa 3, `ThanhVienVIP` tối đa 10 và không phí trễ

### Thư viện
- `ThuVien` **chứa** (composition) danh sách tài liệu và thành viên
- `cho_muon(ma_tv, ma_tl)` kiểm tra: tài liệu có sẵn, thành viên chưa quá hạn mức
- `tra(ma_tv, ma_tl, so_ngay_tre=0)` trả về phí phải đóng
- `bao_cao()` trả về chuỗi thống kê: số tài liệu theo loại, ai đang mượn gì

### Lưu dữ liệu
- `luu(duong_dan)` và `tai(duong_dan)` dùng `json` (thư viện chuẩn)

## Thiết kế mong đợi

```
TaiLieu (ABC)                 ThuVien
├── Sach                      ├── kho: list[TaiLieu]        ← composition
├── Bao                       └── thanh_vien: list[ThanhVien]
└── DiaDVD
                              ThanhVien
                              ├── ThanhVienThuong           ← kế thừa
                              └── ThanhVienVIP
```

Lưu ý về thiết kế: `TaiLieu → Sach` là kế thừa vì quan hệ is-a **bất biến**
(một quyển sách không bao giờ thành DVD). `ThuVien → kho` là composition vì
số lượng thay đổi liên tục.

## Gợi ý thứ tự làm

1. `tai_lieu.py` — abstract class và 3 lớp con. Chạy `python tai_lieu.py` để tự test.
2. `thanh_vien.py` — `ThanhVien` và 2 lớp con.
3. `thu_vien.py` — class điều phối, phần khó nhất.
4. `main.py` — kịch bản sử dụng.

Mỗi file có khối tự kiểm riêng ở cuối, chạy được độc lập.

## Mở rộng (nếu còn hứng)

- Đặt trước tài liệu đang có người mượn (hàng đợi)
- Lịch sử mượn/trả của từng thành viên
- `TaiLieuSo` không giới hạn số bản — thiết kế lại `cho_muon()` thế nào?
