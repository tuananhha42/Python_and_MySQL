import mysql.connector
# Tạo đối tượng connection
def Create_DB():
    myconn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root'
    )
    print("Connect to MySQL Database")
    # Tạo đối tượng cursor
    cur = myconn.cursor()


    cur.execute("DROP DATABASE IF EXISTS assm1_database")
    cur.execute("CREATE DATABASE assm1_database")
    cur.execute("SHOW DATABASES")
    myconn.close()


def Create_Table1():
    myconn1 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
    )
    print("Connect to MySQL Database")
    # Tạo đối tượng cursor
    cur1 = myconn1.cursor()
    cur1.execute('Drop table if exists HocVien')
    cur1.execute('Drop table if exists MonHoc')
    cur1.execute('SET SQL_SAFE_UPDATES = 0')
    cur1.execute('set FOREIGN_KEY_CHECKS = 0')

    #Tạo table
    sql = """ 
        Create table HocVien(
                MaHocVien VARCHAR(20) PRIMARY KEY,
                HoTen VARCHAR(30) NOT NULL ,
                NgaySinh VARCHAR(20) NOT NULL,
                GioiTinh ENUM('0','1') NOT NULL,
                DiaChi VARCHAR(20) NOT NULL,
                SoDienThoai VARCHAR(15) NOT NULL,
                Email VARCHAR(50) NOT NULL UNIQUE KEY
                );
            
        Create table MonHoc(
                MaMonHoc VARCHAR(20) PRIMARY KEY,
                TenMonHoc VARCHAR(20) NOT NULL
                );
        """
    
    cur1.execute(sql)
        
    myconn1.close()


def Create_Table2():
    myconn1 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
    )
    print("Connect to MySQL Database")
    # Tạo đối tượng cursor
    cur1 = myconn1.cursor()
    cur1.execute('Drop table if exists DiemThi')
    cur1.execute('SET SQL_SAFE_UPDATES = 0')
    cur1.execute('set FOREIGN_KEY_CHECKS = 0')

    #Tạo table
    sql = """     
        Create table DiemThi(
                MaHocVien VARCHAR(20) NOT NULL,
                MaMonHoc VARCHAR(20) NOT NULL,
                DiemQuaTrinh TINYINT NOT NULL,
                DiemKetThuc TINYINT NOT NULL,
                FOREIGN KEY(MaHocVien) REFERENCES HocVien(MaHocVien) ON DELETE CASCADE ,
                FOREIGN KEY(MaMonHoc) REFERENCES MonHoc(MaMonHoc) ON DELETE CASCADE 
                );
        """
    
    cur1.execute(sql)
        
    myconn1.close()


def insert_values():
    myconn2 = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database ='assm1_database'
    )

    print("Connect to MySQL Database")
    # tạo đối tượng cursor
    cur = myconn2.cursor()
    
    # Câu lệnh SQL để tạo bảng
    sql = ("""
    INSERT INTO HocVien(MaHocVien,HoTen,NgaySinh,GioiTinh,DiaChi,SoDienThoai,Email)
    VALUES (%s, %s,%s,%s,%s,%s,%s)
    """)
    vals = [("PY000005","Nguyễn Phương Thảo","08/09/1995",'0',"Hà Nội","0964330956","nguyenthao.npt98@gmail.com"),
            ("PY000008","Phạm Ngọc Hoàng","28/12/1971",'1',"Việt Nam","0913677171","hoangdigan@gmail.com"),
            ("PY000013","Trần Nguyễn Thùy Dương","27/03/1995",'0',"Hàn Quốc","1030852703","nguyetnhu1995@gmail.com")]
    
    sql1 = ("""
    INSERT INTO MonHoc(MaMonHoc, TenMonHoc)
    VALUES (%s, %s)
    """)
    vals1 = [("PY1","Python"),
            ("JV1","Java"),
            ("MSQL1","My SQL")]
    
    
    sql2 = ("""
    INSERT INTO DiemThi(MaHocVien,MaMonHoc,DiemQuaTrinh, DiemKetThuc)
    VALUES (%s, %s,%s, %s)
    """)
    vals2 = [("PY000005","PY1",6,9),
            ("PY000008","PY1",10,5),
            ("PY000013","MSQL1",7,8)]

    cur.executemany(sql, vals)
    cur.executemany(sql1, vals1)
    cur.executemany(sql2, vals2)
    # Xác nhận thay đổi
    myconn2.commit()
    # Đóng kết nối
    myconn2.close()



class Menu():
    print("===Menu===")

    def menu(self):
        print("===CHƯƠNG TRÌNH QUẢN LÝ THÔNG TIN ===")
        print("1. Quản lý thông tin học viên")
        print("2. Quản lý thông tin môn học")
        print("3. Quản lý thông tin điểm thi")
        print("0. Thoát chương trình")

    def menu_1(self):
        print("=== QUẢN LÝ THÔNG TIN HỌC VIÊN===")
        print("1. Thêm học viên")
        print("2. Sửa thông tin học viên")
        print("3. Xóa học viên")
        print("4. Tìm kiếm học viên")
        print("5. Hiển thị danh sách học viên")
        print("0. Thoát ")

    def menu_2(self):
        print("===QUẢN LÝ THÔNG TIN MÔN HỌC===")
        print("1. Thêm môn học")
        print("2. Sửa thông tin môn học")
        print("3. Xóa môn học")
        print("4. Tìm kiếm môn học")
        print("5. Hiển thị danh sách môn học")
        print("0. Thoát ")

    def menu_3(self):
        print("===QUẢN LÝ THÔNG TIN ĐIỂM THI===")
        print("1. Thêm điểm thi")
        print("2. Sửa điểm thi")
        print("3. Xóa điểm thi")
        print("4. Tra cứu điểm thi theo mã hoặc họ tên")
        print("5. Hiển thị danh sách điểm thi")
        print("0. Thoát ")

class HocVien():
    def __init__(self):
        pass

    def them_hoc_vien(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma hoc vien: ")
        b = input("Nhap ho ten: ")
        c = input("Nhap ngay sinh: ")
        d = input("Nhap gioi tinh: ")
        e = input("Nhap dia chi: ")
        f = input("Nhap so dien thoai: ")
        g = input("Nhap email: ")

        # Câu lệnh SQL để tạo bảng
        sql = ("""
        INSERT INTO HocVien(MaHocVien,HoTen,NgaySinh,GioiTinh,DiaChi,SoDienThoai,Email)
        VALUES (%s, %s,%s,%s,%s,%s,%s)
        """)
        vals = [(a,b,c,d,e,f,g)]
        cur.executemany(sql, vals)
        myconn2.commit()
        # Đóng kết nối
        myconn2.close()


    def sua_hoc_vien(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma hoc vien muon update ")
        b = input("Nhap vi tri muon update:")
        c = input("Nhap Data moi de update")
        sql ="UPDATE HocVien SET %s = %s WHERE MaHocVien = %s"
        val = (b,c,a)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def xoa_hoc_vien(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap vi tri muon xoa ")
        b = input("Nhap data tai vi tri muon xoa:")
        sql ="DELETE from HocVien WHERE %s = %s "
        val = (a,b)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def timKiem_hoc_vien(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap vi tri muon tim ")
        b = input("Nhap data tai vi tri muon tim:")
        sql ="SELECT * FROM HocVien WHERE %s = %s "
        val = (a,b)
        cur.execute(sql,val)

        result = cur.fetchall()
        for x in result:
            print(x)
        
        myconn2.close()

    def hienThi_hoc_vien(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
    
        sql ="SELECT * FROM HocVien "

        cur.execute(sql)
        result = cur.fetchall()
        print("Hien thi danh sach hoc vien")
        for x in result:
            print(x)
        
        myconn2.close()

class MonHoc():
    def __init__(self):
        pass

    def them_mon_hoc(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma mon hoc: ")
        b = input("Nhap ten mon hoc: ")
        # Câu lệnh SQL để tạo bảng
        sql = ("""
        INSERT INTO MonHoc(MaMonHoc, TenMonHoc)
        VALUES (%s, %s)
        """)
        vals = [(a,b)]
        cur.executemany(sql, vals)
        myconn2.commit()
        # Đóng kết nối
        myconn2.close()

    def sua_mon_hoc(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma mon hoc muon update ")
        b = input("Nhap vi tri muon update:")
        c = input("Nhap Data moi de update")
        sql ="UPDATE MonHoc SET %s = %s WHERE MaMonHoc = %s"
        val = (b,c,a)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def xoa_mon_hoc(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap vi tri muon xoa ")
        b = input("Nhap data tai vi tri muon xoa:")
        sql ="DELETE from MonHoc WHERE %s = %s "
        val = (a,b)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def timKiem_mon_hoc(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap vi tri muon tim ")
        b = input("Nhap data tai vi tri muon tim:")
        sql ="SELECT * FROM MonHoc WHERE %s = %s "
        val = (a,b)
        cur.execute(sql,val)

        result = cur.fetchall()
        for x in result:
            print(x)
        
        myconn2.close()

    def hienThi_mon_hoc(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
    
        sql ="SELECT * FROM MonHoc "

        cur.execute(sql)
        result = cur.fetchall()
        print("Hien thi danh sach mon hoc")
        for x in result:
            print(x)
        
        myconn2.close()

class DiemThi():
    def __init__(self):
        pass

    def them_diem_thi(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma hoc vien: ")
        b = input("Nhap ma mon hoc: ")
        c = int(input("Nhap diem qua trinh:"))
        d = int(input("Nhap diem ket thuc:"))
        # Câu lệnh SQL để tạo bảng
        sql = ("""
        INSERT INTO DiemThi(MaHocVien, MaMonHoc,DiemQuaTrinh, DiemKetThuc)
        VALUES (%s, %s, %s, %s)
        """)
        vals = [(a,b,c,d)]
        cur.executemany(sql, vals)
        myconn2.commit()
        # Đóng kết nối
        myconn2.close()

    def sua_diem_thi(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ma mon hoc muon update ")
        a1 = input("Nhap ma hoc vien muon update")
        b = input("Nhap vi tri muon update:")
        c = input("Nhap Data moi de update")
        sql ="UPDATE DiemThi SET %s = %s WHERE MaMonHoc = %s OR MaHocVien = %s"
        val = (b,c,a,a1)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def xoa_diem_thi(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap vi tri muon xoa ")
        b = input("Nhap data tai vi tri muon xoa:")
        sql ="DELETE from DiemThi WHERE %s = %s "
        val = (a,b)
        cur.execute(sql,val)

        myconn2.commit()
        
        myconn2.close()

    def timKiem_diem_thi(self):
        myconn2 = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        database ='assm1_database'
        )

        print("Connect to MySQL Database")
        # tạo đối tượng cursor
        cur = myconn2.cursor()
        a = input("Nhap ten hoc vien muon tim ")
        b = input("Nhap ma hoc vien muon tim:")
        sql ="""SELECT * FROM DiemThi
                JOIN HocVien ON DiemThi.MaHocVien = HocVien.MaHocVien
                WHERE TenHocVien = %s OR MaHocVien = %s """
        val = (a,b)
        cur.execute(sql,val)

        result = cur.fetchall()
        for x in result:
            print(x)
        
        myconn2.close()

    def hienThi_diem_thi(self):
        pass

def xuly_1():
    hocvien = HocVien()
    while True:
        menu.menu_1()
        choice2 = int(input("Nhập lựa chọn của bạn (0-5): "))
        if choice2 == 0:
            print("Trở về")
            break
        elif choice2 == 1:
            hocvien.them_hoc_vien()
        elif choice2 == 2:
            hocvien.sua_hoc_vien()
        elif choice2 == 3:
            hocvien.xoa_hoc_vien()
        elif choice2 == 4:
            hocvien.timKiem_hoc_vien()
        elif choice2 == 5:
            hocvien.hienThi_hoc_vien()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

def xuly_2():
    monhoc = MonHoc()
    while True:
        menu.menu_2()
        choice3 = int(input("Nhập lựa chọn của bạn (0-5): "))
        if choice3 == 0:
            print("Trở về")
            break
        elif choice3 == 1:
            monhoc.them_mon_hoc()
        elif choice3 == 2:
            monhoc.sua_mon_hoc()
        elif choice3 == 3:
            monhoc.xoa_mon_hoc()
        elif choice3 == 4:
            monhoc.timKiem_mon_hoc()
        elif choice3 == 5:
            monhoc.hienThi_mon_hoc()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


def xuly_3():
    diemthi = DiemThi()
    while True:
        menu.menu_3()
        choice4 = int(input("Nhập lựa chọn của bạn (0-5): "))
        if choice4 == 0:
            print("Trở về")
            break
        elif choice4 == 1:
            diemthi.them_diem_thi()
        elif choice4 == 2:
            diemthi.sua_diem_thi()
        elif choice4 == 3:
            diemthi.xoa_diem_thi()
        elif choice4 == 4:
            diemthi.timKiem_diem_thi()
        elif choice4 == 5:
            diemthi.hienThi_diem_thi()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")




if __name__ == "__main__":
    Create_DB()
    Create_Table1()
    Create_Table2()
    insert_values()
    menu = Menu()
    while True:
        menu.menu()
        choice = int(input("Nhập lựa chọn của bạn (0-3): "))
        print()

        if choice == 0:
            print("Đã thoát chương trình.")
            break
        elif choice == 1:
            xuly_1()

        elif choice == 2:
            xuly_2()

        elif choice == 3:
            xuly_3()
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

