from icecream import ic
from tabulate import tabulate

class QuanLyHocVien():
    def __init__(self, db):
        self.cur = db.cur
        self.conn = db.conn

    def them(self):
        id = input("Nhập mã học viên: ")
        name = input("Nhập họ tên: ")
        date_of_birth = input("Nhập ngày sinh (dd/mm/yyyy): ")
        gender = input("Nhập giới tính: ")
        address = input("Nhập địa chỉ: ")
        phone = input("Nhập số điện thoại: ")
        email = input("Nhập email: ")
        try:
            # Thực hiện truy vấn INSERT vào database
            sql = "INSERT INTO students (id, name, date_of_birth, gender, address, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (int(id), name, date_of_birth, gender, address, phone, email)
            self.cur.execute(sql, values)
            self.conn.commit()

            print("Thêm học viên thành công.")
        except:
            print("Du lieu dau vao khong hop le")

    def sua(self):
        id = input("Nhập mã học viên cần sửa thông tin: ")
        try:
            # Kiểm tra học viên có tồn tại không
            sql = "SELECT * FROM students WHERE id = %s"
            value = [id]
            self.cur.execute(sql, value)

            result = self.cur.fetchone()

            if result is None:
                print("Không tìm thấy học viên.")
                return

            name = input("Nhập họ tên: ")
            date_of_birth = input("Nhập ngày sinh (yyyy-mm-dd): ")
            gender = input("Nhập giới tính: ")
            address = input("Nhập địa chỉ: ")
            phone = input("Nhập số điện thoại: ")
            email = input("Nhập email: ")

            # Thực hiện truy vấn UPDATE vào database
            sql = "UPDATE students SET name = %s, date_of_birth = %s, gender = %s, address = %s, phone = %s, email = %s WHERE id = %s"
            values = (name, date_of_birth, gender, address, phone, email, id)
            self.cur.execute(sql, values)
            self.conn.commit()

            print("Sửa thông tin học viên thành công.")
        except:
            print("Du lieu dau vao khong hop le!")

    def xoa(self):
        id = input("Nhập mã học viên cần xóa: ")

        try:
            sql = "SELECT * FROM students WHERE id=%s"
            value = [id]
            self.cur.execute(sql, value)
            result = self.cur.fetchone()
            if result is None:
                print("Không tìm thấy học viên.")
                return


            sql = "DELETE FROM students WHERE id = %s"
            value = [id]
            self.cur.execute(sql, value)
            self.conn.commit()

            print("Xoá học viên thành công.")
        except:
            print("Du lieu dau vao khong hop le!")

    def timKiem(self):
        keyword = input("Nhập mã học viên hoặc họ tên học viên cần tìm: ")
        try:
            if self.check_id(keyword):
                id = keyword
                # Thực hiện truy vấn SELECT vào database
                sql = "SELECT * FROM students WHERE id = %s"
                value = [id]
                
            else:
                name = keyword
                # Thực hiện truy vấn SELECT vào database
                sql = "SELECT * FROM students WHERE name = %s"
                value = [name]

            self.cur.execute(sql, value)
            result = self.cur.fetchall()

            if result is None:
                print("Không tìm thấy học viên.")
                return
                
            self.tabulate_print(result)
        except:
            print("Du lieu dau vao khong hop le!")

    def check_id(self, id):
        try:
            id = int(id)
            return True
        except:
            print("")

        return False
    
    def hienThi(self):
        print("Danh sách học viên:")
        sql = "SELECT * FROM students"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results is None:
            print("Không tìm thấy học viên.")
            return
        
        self.tabulate_print(results)

    def tabulate_print(self, data):
        headers = ["Mã học viên", "Họ tên", "Ngày sinh", "Giới tính", "Địa chỉ", "Số điện thoại", "Email"]
        print(tabulate(data, headers, tablefmt="grid"))