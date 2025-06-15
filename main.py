from xu_ly_kho import *
from doc_ghi_file import doc_file, luu_file

def menu():
    kho = doc_file()

    while True:
        print("\n" + "=" * 65)
        print("CHƯƠNG TRÌNH QUẢN LÝ KHO HÀNG CÔNG TY THIẾT BỊ NỘI THẤT VIGLACERA")
        print("=" * 65)
        print("| {:<2} | {:<50} |".format("1", "Thêm sản phẩm"))
        print("| {:<2} | {:<50} |".format("2", "Xóa sản phẩm theo mã"))
        print("| {:<2} | {:<50} |".format("3", "Cập nhật sản phẩm"))
        print("| {:<2} | {:<50} |".format("4", "Tìm kiếm theo tên"))
        print("| {:<2} | {:<50} |".format("5", "Hiển thị toàn bộ sản phẩm"))
        print("| {:<2} | {:<50} |".format("6", "Lưu dữ liệu vào file"))
        print("| {:<2} | {:<50} |".format("7", "Hiển thị theo danh mục"))
        print("| {:<2} | {:<50} |".format("8", "Thống kê tổng giá trị hàng tồn"))
        print("| {:<2} | {:<50} |".format("9", "Danh sách sản phẩm sắp hết hàng"))
        print("| {:<2} | {:<50} |".format("10", "Xuất hóa đơn theo mã sản phẩm"))
        print("| {:<2} | {:<50} |".format("11", "Lọc sản phẩm theo khoảng giá"))
        print("| {:<2} | {:<50} |".format("0", "Thoát"))
        print("=" * 65)

        chon = input("Nhập lựa chọn (0–11): ").strip()

        if chon == "1":
            them_san_pham(kho)
        elif chon == "2":
            ma = input("Nhập mã sản phẩm cần xóa: ")
            xoa_san_pham(kho, ma)
        elif chon == "3":
            ma = input("Nhập mã sản phẩm cần cập nhật: ")
            cap_nhat_san_pham(kho, ma)
        elif chon == "4":
            tu_khoa = input("Nhập từ khóa tên sản phẩm: ")
            tim_kiem_san_pham(kho, tu_khoa)
        elif chon == "5":
            hien_thi(kho)
        elif chon == "6":
            luu_file(kho)
        elif chon == "7":
            loai = input("Nhập tên danh mục: ")
            hien_thi_theo_loai(kho, loai)
        elif chon == "8":
            thong_ke_gia_tri_ton_kho(kho)
        elif chon == "9":
            san_pham_sap_het_hang(kho)
        elif chon == "10":
            ma = input("Nhập mã sản phẩm cần in hóa đơn: ")
            xuat_hoa_don(kho, ma)
        elif chon == "11":
            min_gia = float(input("Giá thấp nhất: "))
            max_gia = float(input("Giá cao nhất: "))
            loc_theo_khoang_gia(kho, min_gia, max_gia)
        elif chon == "0":
            luu_file(kho)
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    menu()

