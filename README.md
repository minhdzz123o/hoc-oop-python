# Lộ trình học OOP bằng Python

Dành cho người mới bắt đầu lập trình. Chỉ dùng thư viện chuẩn của Python — không cần cài gì thêm.

## Cách chạy

Mỗi file ví dụ chạy độc lập được:

```bash
python 00-nen-tang/02_ham.py
```

File trong `baitap/` có `assert` tự kiểm. **Lúc đầu nó sẽ báo lỗi** — đó là đúng, vì chỗ trống chưa làm.
Làm xong bài, chạy lại thấy `TẤT CẢ BÀI TẬP ĐÚNG` là bạn đã hoàn thành.

## Lộ trình

### Chặng A — Nền tảng (tuần 1–2)

OOP không phải điểm bắt đầu. Nó là cách tổ chức code khi code đã đủ lớn.
Chặng này xây nền: hàm, list, dict. Đi nhanh nhưng đừng bỏ.

| Tuần | File | Nội dung |
|---|---|---|
| 1 | `00-nen-tang/01_bien_dieu_kien_vonglap.py` | biến, kiểu, if/else, for, while |
| 1 | `00-nen-tang/02_ham.py` | tham số, return, scope, mutable argument |
| 2 | `00-nen-tang/03_list_dict.py` | list, dict, comprehension |
| 2 | `00-nen-tang/04_dict_lam_doi_tuong.py` | **file quan trọng nhất chặng A** — tạo nhu cầu cho class |

### Chặng B — OOP (tuần 3–8)

| Tuần | Chương | Nội dung |
|---|---|---|
| 3 | `01-class-object/` | class & object, `__init__`, `self`, method |
| 4 | `02-encapsulation/` | `_private`, `@property` |
| 5 | `03-inheritance/` | `super()`, override |
| 6 | `04-polymorphism/` | đa hình, duck typing — **phần giá trị nhất của OOP** |
| 7 | `05-abstraction/` + `06-composition/` | `abc.ABC`, `Protocol`, composition vs inheritance |
| 8 | `07-pythonic/` | dunder methods, `@dataclass`, `@classmethod` |

### Dự án

- `duan/quan-ly-thu-vien/` — làm sau tuần 7
- `duan/game-caro/` — làm sau tuần 8

## Lưu ý quan trọng

**Đừng nhảy qua tuần 4 (encapsulation) để tới tuần 5 (inheritance).**
Kế thừa mà không hiểu đóng gói là nguồn gốc của phần lớn code OOP tệ.

**Đừng dừng ở tuần 5.** Nhiều người học tới kế thừa rồi tưởng đã xong OOP, sau đó lạm dụng
kế thừa — tạo cây 5–6 tầng. Thực tế composition (tuần 7) và polymorphism (tuần 6) được
dùng nhiều hơn kế thừa rất nhiều.

## Sau lộ trình này

SOLID → design patterns (Factory, Strategy, Observer) → viết unit test cho class bằng `pytest`.
