# Dự án 2 — Game caro trên terminal

Làm sau khi xong tuần 8. Dự án này dùng: class, dunder methods,
abstract class, composition, polymorphism.

## Chạy

```bash
python main.py
```

Lúc đầu báo lỗi ở các `TODO`. Khi xong, bạn chơi được với máy ngay trong terminal.

## Yêu cầu chức năng

### `BanCo` (file `ban_co.py`)
- Lưới `n x n`, mặc định 3x3 (tic-tac-toe), hỗ trợ được 5x5 với điều kiện
  thắng 4 quân liên tiếp
- `__str__` in bàn cờ có số hàng/cột để người chơi biết nhập gì
- `__getitem__` cho phép `ban_co[1, 2]` đọc một ô
- `dat(hang, cot, quan)` — chặn ô đã có quân và toạ độ ngoài bàn
- `o_trong()` trả list các ô còn trống
- `nguoi_thang()` trả `"X"`, `"O"` hoặc `None`
- `hoa()` — hết ô mà chưa ai thắng

### Người chơi (file `nguoi_choi.py`)
- `NguoiChoi` là **abstract class** với `@abstractmethod chon_o(ban_co)`
- `NguoiChoiNguoi` đọc từ bàn phím, nhập lại nếu sai
- `MayNgauNhien` chọn ô trống bất kỳ
- `MayThongMinh` theo thứ tự ưu tiên: thắng ngay được thì thắng → chặn
  nước thắng của đối thủ → chiếm trung tâm → chiếm góc → ngẫu nhiên

> Ba lớp người chơi trên là ví dụ rõ nhất của đa hình trong dự án này:
> `TroChoi` gọi `chon_o()` mà không cần biết đó là người hay máy loại nào.

### `TroChoi` (file `tro_choi.py`)
- **Chứa** một `BanCo` và hai người chơi (composition)
- `choi_mot_luot()` — một lượt đi
- `chay()` — vòng lặp tới khi có kết quả, trả về người thắng hoặc `None`
- Có chế độ `im_lang=True` để test được mà không in gì

## Thiết kế mong đợi

```
NguoiChoi (ABC)              TroChoi
├── NguoiChoiNguoi           ├── ban_co: BanCo        ← composition
├── MayNgauNhien             └── nguoi_choi: list     ← composition
└── MayThongMinh
```

`TroChoi` dùng composition vì ta muốn **đổi** người chơi, bàn cờ, luật thắng
mà không tạo class mới. Thử nghĩ: nếu `TroChoi` kế thừa `BanCo` thì làm sao
đổi sang bàn 5x5 giữa lúc chạy?

## Gợi ý thứ tự làm

1. `ban_co.py` — làm xong và chạy tự kiểm trước. Đây là nền.
2. `nguoi_choi.py` — `MayNgauNhien` trước, `MayThongMinh` sau.
3. `tro_choi.py` — điều phối.
4. `main.py` — đã viết sẵn, chỉ chạy.

## Mở rộng

- Bàn 5x5, thắng 4 quân — `BanCo` của bạn có cần sửa không? Nếu phải sửa
  nhiều thì thiết kế ban đầu chưa đủ linh hoạt.
- `MayMinimax` chơi hoàn hảo trên bàn 3x3
- Lưu/đọc ván đang chơi bằng JSON
- Đổi luật thắng thành một object riêng (`LuatThang`) — composition thay vì
  viết cứng trong `BanCo`
