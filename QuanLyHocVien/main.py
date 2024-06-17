from quanly.Menu import Menu
from quanly.DB import QuanLyDB
from quanly.Students import QuanLyHocVien
from quanly.Courses import QuanLyMonHoc
from quanly.Grades import QuanLyDiemThi

def xuly_1(qlhv):
    while True:
        menu.menu_1()
        choice = input("Nhập lựa chọn của bạn (0-5): ")
        if choice == "0":
            print("Trở về")
            break
        elif choice == "1": 
            print("Thêm học viên")
            qlhv.them()

        elif choice == "2":  
            print("Sửa thông tin học viên")
            qlhv.sua()

        elif choice == "3":  
            print("Xóa học viên")
            qlhv.xoa()
        elif choice == "4": 
            print("Tìm kiếm học viên")
            qlhv.timKiem()
        elif choice == "5": 
            print("Hiển thị danh sách học viên")
            qlhv.hienThi()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

def xuly_2(qlmh):
    while True:
        menu.menu_2()
        choice = input("Nhập lựa chọn của bạn (0-5): ")
        if choice == "0":
            print("Trở về")
            break
        elif choice == "1": 
            qlmh.them()
        elif choice == "2":
            qlmh.sua()
        elif choice == "3":
            qlmh.xoa()
        elif choice == "4": 
            qlmh.timKiem()
        elif choice == "5": 
            qlmh.hienThi()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

def xuly_3(qldt):
    while True:
        menu.menu_3()
        choice = input("Nhập lựa chọn của bạn (0-5): ")
        if choice == "0":
            print("Trở về")
            break
        elif choice == "1":
            qldt.them()
        elif choice == "2":
            qldt.sua()
        elif choice == "3":
            qldt.xoa()
        elif choice == "4":
            qldt.timKiem()
        elif choice == "5":
            qldt.hienThi()
        elif choice == "6":
            qldt.thongKe()
        elif choice == "7":
            menu.menu4()
            choice = input("Nhập lựa chọn của bạn: ")

            if choice == "1":
                qldt.export_all_grades_to_excel()
            elif choice == "2":
                qldt.export_grade_A_to_excel()
            elif choice == "3":
                qldt.export_grade_B_to_excel()
            elif choice == "4":
                qldt.export_grade_C_to_excel()
            elif choice == "5":
                qldt.export_grade_D_to_excel()
            elif choice == "0":
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


if __name__ == "__main__" :
    menu = Menu()
    db = QuanLyDB()
    name_db = 'asm2_DB'

    if not db.check_database_exists(name_db) :  
        db.delete_DB(name_db)      
        db.create_DB(name_db)
        db.ceate_table(name_db)
    else:
        db.connect_DB(name_db)


    while True:
        menu.menu()
        choice = input("Nhập lựa chọn của bạn (0-3): ")
        print()

        if choice == "0":
            print("Đã thoát chương trình.")
            db.close_db()
            break
        elif choice == "1":
            qlhv = QuanLyHocVien(db)
            xuly_1(qlhv)

        elif choice == "2":
            qlmh = QuanLyMonHoc(db)
            xuly_2(qlmh)
            
        elif choice == "3":
            qldt = QuanLyDiemThi(db)
            xuly_3(qldt)
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")