from icecream import ic
from tabulate import tabulate

class QuanLyMonHoc():
    def __init__(self, db):
        self.cur = db.cur
        self.conn = db.conn

    def them(self):
        id = input("Nhập mã môn học: ")
        name = input("Nhập tên môn học: ")

        try:
            # Thực hiện truy vấn INSERT vào database
            sql = "INSERT INTO courses (id, name) VALUES (%s, %s)"
            values = (int(id), name)
            self.cur.execute(sql, values)
            self.conn.commit()

            print("Thêm môn học thành công.")
        except:
            print("Du lieu dau vao khong hop le!")

    def sua(self):
        id = input("Nhập mã môn học muốn sửa: ")
        try:
            # Kiểm tra môn học có tồn tại không
            sql = "SELECT * FROM courses WHERE id = %s"
            value = [id]
            self.cur.execute(sql, value)

            result = self.cur.fetchone()

            if result is None:
                print("Không tìm thấy môn học.")
                return
            name = input("Nhập tên môn học: ")

            # Thực hiện truy vấn UPDATE vào database
            sql = "UPDATE courses SET name = %s WHERE id = %s"
            values = (name, id)
            self.cur.execute(sql, values)
            self.conn.commit()

            print("Sửa thông tin môn học thành công.")
        except:
            print("Du lieu dau vao khong hop le!")
    def xoa(self):
        id = input("Nhập mã môn học muốn xoá: ")

        try:
            sql = "SELECT * FROM courses WHERE id=%s"
            value = [id]
            self.cur.execute(sql, value)
            result = self.cur.fetchone()
            if result is None:
                print("Không tìm thấy môn học.")
                return


            sql = "DELETE FROM courses WHERE id = %s"
            value = [id]
            self.cur.execute(sql, value)
            self.conn.commit()

            print("Xoá môn học thành công.")
        except:
            print("Du lieu dau vao khong hop le!")

    def timKiem(self):
        keyword = input("Nhập mã môn học hoặc tên môn học cần tìm: ")
        try:
            if self.check_id(keyword):
                id = keyword
                # Thực hiện truy vấn SELECT vào database
                sql = "SELECT * FROM courses WHERE id = %s"
                value = [id]
                
            else:
                name = keyword
                # Thực hiện truy vấn SELECT vào database
                sql = "SELECT * FROM courses WHERE name = %s"
                value = [name]

            self.cur.execute(sql, value)
            result = self.cur.fetchall()

            if result is None:
                print("Không tìm thấy môn học.")      
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
        print("Danh sách môn học:")
        sql = "SELECT * FROM courses"
        self.cur.execute(sql)
        results = self.cur.fetchall()
        if results is None:
            print("Không tìm thấy môn học.")
            return        
        self.tabulate_print(results)

    def tabulate_print(self, data):
        headers = ["Mã môn học", "Môn Học"]
        print(tabulate(data, headers, tablefmt="grid"))