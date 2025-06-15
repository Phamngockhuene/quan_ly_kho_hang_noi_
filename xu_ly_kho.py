import pandas as pd

def them_san_pham(dskho):
    print("\n--- Nhập thông tin sản phẩm ---")
    ma = input("Mã sản phẩm: ")
    if any(sp[0] == ma for sp in dskho):
        print("Mã sản phẩm đã tồn tại. Vui lòng nhập lại.")
        return
    ten = input("Tên sản phẩm: ")
    loai = input("Loại sản phẩm: ")
    sl = int(input("Số lượng: "))
    gia = float(input("Đơn giá: ").replace('.', '').strip())
    dskho.append([ma, ten, loai, sl, gia])
    print("Đã thêm sản phẩm")

def xoa_san_pham(dskho, ma_xoa):
    truoc = len(dskho)
    dskho[:] = [sp for sp in dskho if sp[0] != ma_xoa]
    print("Đã xóa" if len(dskho) < truoc else "Không tìm thấy mã sản phẩm")

def cap_nhat_san_pham(dskho, ma_sua):
    for sp in dskho:
        if sp[0] == ma_sua:
            ten = input(f"Tên SP ({sp[1]}): ") or sp[1]
            loai = input(f"Loại ({sp[2]}): ") or sp[2]
            try:
                sl = int(input(f"Số lượng ({sp[3]}): ") or sp[3])
                gia = float(input(f"Đơn giá ({sp[4]}): ") or sp[4])
                sp[1], sp[2], sp[3], sp[4] = ten, loai, sl, gia
                print("Đã cập nhật sản phẩm.")
                return
            except:
                print("Lỗi nhập dữ liệu")
                return
    print("Không tìm thấy mã sản phẩm")

def tim_kiem_san_pham(dskho, tu_khoa):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    kq = df[df["Tên SP"].str.contains(tu_khoa, case=False)]
    if kq.empty:
        print("Không tìm thấy sản phẩm")
    else:
        kq.index += 1
        print("\n--- Kết quả tìm kiếm ---")
        print(kq)

def hien_thi(dskho):
    if not dskho:
        print("Kho đang trống")
        return
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    df.index += 1
    print("\n--- Danh sách sản phẩm ---")
    print(df)

def hien_thi_theo_loai(dskho, loai_tim):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    kq = df[df["Loại"].str.lower() == loai_tim.lower()]
    if kq.empty:
        print("Danh mục không tồn tại hoặc không có sản phẩm")
    else:
        kq.index += 1
        print("\n--- Danh sách sản phẩm theo danh mục ---")
        print(kq)

def thong_ke_gia_tri_ton_kho(dskho):
    tong = sum(sp[3] * sp[4] for sp in dskho)
    print(f"Tổng giá trị hàng tồn kho: {tong:,.0f} VND")

def san_pham_sap_het_hang(dskho):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    kq = df[df["Số lượng"] < 5]
    if kq.empty:
        print("Không có sản phẩm nào sắp hết hàng")
    else:
        kq.index += 1
        print("\n--- Sản phẩm sắp hết hàng ---")
        print(kq)

def xuat_hoa_don(dskho, ma):
    for sp in dskho:
        if sp[0] == ma:
            print("\n----- HÓA ĐƠN BÁN HÀNG -----")
            print(f"Mã sản phẩm : {sp[0]}")
            print(f"Tên sản phẩm: {sp[1]}")
            print(f"Loại         : {sp[2]}")
            print(f"Số lượng     : {sp[3]}")
            print(f"Đơn giá      : {sp[4]:,.0f} VND")
            print(f"Thành tiền   : {sp[3] * sp[4]:,.0f} VND")
            return
    print("Không tìm thấy sản phẩm")

def loc_theo_khoang_gia(dskho, min_gia, max_gia):
    df = pd.DataFrame(dskho, columns=["Mã SP", "Tên SP", "Loại", "Số lượng", "Đơn giá"])
    kq = df[(df["Đơn giá"] >= min_gia) & (df["Đơn giá"] <= max_gia)]
    if kq.empty:
        print("Không có sản phẩm trong khoảng giá này")
    else:
        kq.index += 1
        print("\n--- Sản phẩm theo khoảng giá ---")
        print(kq)

