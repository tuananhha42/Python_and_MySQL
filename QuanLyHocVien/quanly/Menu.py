
class Menu():
    """
    Menu chương trình
    """
    def menu(self):
        print("\n=== CHƯƠNG TRÌNH QUẢN LÝ THÔNG TIN ĐIỂM THI ===")
        print("1. Quản lý thông tin Học viên")
        print("2. Quản lý thông tin Môn học")
        print("3. Quản lý thông tin Điểm thi")
        print("0. Thoát chương trình")

    def menu_1(self):
        print("\n=== Quản lý thông tin Học viên ===")
        print("1. Thêm học viên")
        print("2. Sửa thông tin học viên")
        print("3. Xóa học viên")
        print("4. Tìm kiếm học viên")
        print("5. Hiển thị danh sách học viên")
        print("0. Trở về")

    def menu_2(self):
        print("\n=== Quản lý thông tin Môn học ===")
        print("1. Thêm môn học")
        print("2. Sửa thông tin môn học")
        print("3. Xóa môn học")
        print("4. Tìm kiếm môn học")
        print("5. Hiển thị danh sách môn học")
        print("0. Trở về")

    def menu_3(self):
        print("\n=== Quản lý thông tin Điểm thi ===")
        print("1. Thêm điểm thi")
        print("2. Sửa điểm thi")
        print("3. Xóa điểm thi")
        print("4. Tra cứu điểm theo mã học viên hoặc họ tên học viên")
        print("5. Hiển thị danh sách điểm thi") 
        print("6. Thống kê điểm thi")
        print("7. Kết xuất bảng điểm ra tệp tin")
        print("0. Trở về")

    def menu4(self):
        print("===== XUẤT BẢNG ĐIỂM RA TỆP TIN EXCEL =====")
        print("1. Xuất bảng điểm tất cả học viên")
        print("2. Xuất bảng điểm học viên có điểm A")
        print("3. Xuất bảng điểm học viên có điểm B")
        print("4. Xuất bảng điểm học viên có điểm C")
        print("5. Xuất bảng điểm học viên có điểm D")
        print("0. Quay lại")