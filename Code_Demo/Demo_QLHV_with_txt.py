# from typing import int 
from icecream import ic 

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

class HocVien():
    def __init__(self, id, name, date_of_birth, gender, address, phone, email):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email

    def to_string(self):
        return f"{self.id}|{self.name}|{self.date_of_birth}|{self.gender}|{self.address}|{self.phone}|{self.email}"

class QuanLyHocVien():
    def __init__(self, name_file):
        self.name_file = name_file
        self.students = self.read_data()

    def read_data(self):
        """
        file.txt --> list(Hocvien())
        """
        students = []
        try:
            with open(self.name_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split('|')
                    student = HocVien(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
                    students.append(student)
        except FileNotFoundError:
            pass
        return students
    
    def save_data(self, students):
        """
        list(Hocvien()) --> file.txt
        """
        with open(self.name_file, 'w') as file:
            for student in students:
                file.write(student.to_string() + '\n')

    def them(self):
        id = input("Nhập mã học viên: ")
        name = input("Nhập họ tên: ")
        date_of_birth = input("Nhập ngày sinh (dd/mm/yyyy): ")
        gender = input("Nhập giới tính (0-Nam, 1-Nữ): ")
        address = input("Nhập địa chỉ: ")
        phone = input("Nhập số điện thoại: ")
        email = input("Nhập email: ")
        student = HocVien(id, name, date_of_birth, gender, address, phone, email)
        self.students.append(student)
        self.save_data(self.students)
        print("Đã thêm học viên thành công.")

    def sua(self):
        id = input("Nhập mã học viên cần sửa thông tin: ")
        for student in self.students:
            if student.id == id:
                student.name = input("Nhập họ tên mới: ")
                student.date_of_birth = input("Nhập ngày sinh mới (dd/mm/yyyy): ")
                student.gender = input("Nhập giới tính mới (0-Nam, 1-Nữ): ")
                student.address = input("Nhập địa chỉ mới: ")
                student.phone = input("Nhập số điện thoại mới: ")
                student.email = input("Nhập email mới: ")
                self.save_data(self.students)
                print("Đã cập nhật thông tin học viên thành công.")
                return
        print("Không tìm thấy học viên có mã học viên tương ứng.")

    def xoa(self):
        id = input("Nhập mã học viên cần xóa: ")
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                self.save_data(self.students)
                print("Đã xóa học viên thành công.")
                return
        print("Không tìm thấy học viên có mã học viên tương ứng.")

    def timKiem(self):
        keyword = input("Nhập mã học viên hoặc họ tên học viên cần tìm: ")
        found_students = []
        for student in self.students:
            if keyword == student.id or keyword == student.name:
                found_students.append(student)
        if found_students:
            print("Kết quả tìm kiếm:")
            for student in found_students:
                print(f"Mã học viên: {student.id}, Họ tên: {student.name}, Ngày sinh: {student.date_of_birth}, Giới tính: {student.gender}, Địa chỉ: {student.address}, Số điện thoại: {student.phone}, Email: {student.email}")
        else:
            print("Không tìm thấy học viên.")

    def hienThi(self):
        print("Danh sách học viên:")
        for student in self.students:
            print(f"Mã học viên: {student.id}, Họ tên: {student.name}, Ngày sinh: {student.date_of_birth}, Giới tính: {student.gender}, Địa chỉ: {student.address}, Số điện thoại: {student.phone}, Email: {student.email}")

class MonHoc():
    def __init__(self,id, name):
        self.id = id
        self.name = name

    def to_string(self):
        return f"{self.id}|{self.name}"
    
class QuanLyMonHoc():
    def __init__(self, name_file) -> None:
        self.name_file = name_file
        self.courses = self.load_data()

    def load_data(self):
        courses = []
        try:
            with open(self.name_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split('|')
                    course = MonHoc(data[0], data[1])
                    courses.append(course)
        except FileNotFoundError:
            pass
        return courses
    
    def save_data(self):
        with open(self.name_file, 'w') as file:
            for course in self.courses:
                file.write(course.to_string() + '\n')

    def them(self):
        id = input("Nhập mã môn học: ")
        name = input("Nhập tên môn học: ")
        course = MonHoc(id, name)
        self.courses.append(course)
        self.save_data()
        print("Đã thêm môn học thành công.")

    def sua(self):
        id = input("Nhập mã môn học cần sửa thông tin: ")
        for course in self.courses:
            if course.id == id:
                course.name = input("Nhập tên môn học mới: ")
                self.save_data()
                print("Đã cập nhật thông tin môn học thành công.")
                return
        print("Không tìm thấy môn học có mã môn học tương ứng.")

    def xoa(self):
        id = input("Nhập mã môn học cần xóa: ")
        for course in self.courses:
            if course.id == id:
                self.courses.remove(course)
                self.save_data()
                print("Đã xóa môn học thành công.")
                return
        print("Không tìm thấy môn học có mã môn học tương ứng.")

    def timKiem(self):
        keyword = input("Nhập mã môn cần tìm: ")
        found_course = []
        for course in self.courses:
            if keyword == course.id:
                found_course.append(course)
        if found_course:
            print("Kết quả tìm kiếm:")
            for course in found_course:
                print(f"Mã môn học: {course.id}, Tên môn học: {course.name}")
        else:
            print("Không tìm thấy học viên.")
        # pass

    def hienThi(self):
        print("Danh sách môn học:")
        for course in self.courses:
            print(f"Mã môn học: {course.id}, Tên môn học: {course.name}")
        
class DiemThi():
    def __init__(self, student_id, course_id, midterm_score, final_score):
        self.student_id = student_id
        self.course_id = course_id
        self.midterm_score = midterm_score
        self.final_score = final_score

    def to_string(self):
        return f"{self.student_id}|{self.course_id}|{self.midterm_score}|{self.final_score}"

class QuanLyDiemThi():
    def __init__(self, file_demthi, file_monhoc, file_hocvien) -> None:
        self.name_file = file_demthi
        self.scores = self.load_data()

        self.qlhv = QuanLyHocVien(file_hocvien)
        self.students = self.qlhv.students
        self.qlmh = QuanLyMonHoc(file_monhoc)
        self.courses = self.qlmh.courses

    def load_data(self):
        scores = []
        try:
            with open(self.name_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split('|')
                    score = DiemThi(data[0], data[1], float(data[2]), float(data[3]))
                    scores.append(score)
        except FileNotFoundError:
            pass
        return scores
    
    def save_data(self):
        with open(self.name_file, 'w') as file:
            for score in self.scores:
                file.write(score.to_string() + '\n')

    def them(self):
        student_id = input("Nhập mã học viên: ")
        course_id = input("Nhập mã môn học: ")
        
        dk1 = any(student_id == student.id for student in self.students)
        dk2 = any(course_id == course.id for course in self.courses)

        if dk1 and dk2:
            midterm_score = float(input("Nhập điểm quá trình: "))
            final_score = float(input("Nhập điểm kết thúc: "))
            score = DiemThi(student_id, course_id, midterm_score, final_score)
            self.scores.append(score)
            self.save_data()
            print("Đã thêm điểm thi thành công.")
        elif dk1 == False : 
            print(f"Không tồn tại mã môn học viên : {student_id}")
        elif dk2 == False : 
            print(f"Không tồn tại mã môn học : {course_id}")

    def sua(self):
        student_id = input("Nhập mã học viên: ")
        course_id = input("Nhập mã môn học: ")
        for score in self.scores:
            if score.student_id == student_id and score.course_id == course_id:
                score.midterm_score = float(input("Nhập điểm quá trình mới: "))
                score.final_score = float(input("Nhập điểm kết thúc mới: "))
                self.save_data()
                print("Đã cập nhật điểm thi thành công.")
                return
        print("Không tìm thấy điểm thi cho học viên và môn học tương ứng.")

    def xoa(self):
        student_id = input("Nhập mã học viên: ")
        course_id = input("Nhập mã môn học: ")
        for score in self.scores:
            if score.student_id == student_id and score.course_id == course_id:
                self.scores.remove(score)
                self.save_data()
                print("Đã xóa điểm thi thành công.")
                return
        print("Không tìm thấy điểm thi cho học viên và môn học tương ứng.")

    def timKiem(self):
        keyword = input("Nhập mã học viên hoặc họ tên học viên: ")
        found_scores = []
        for score in self.scores:
            for student in self.students:
                if keyword == student.id or keyword == student.name:
                    if score.student_id == student.id:
                        found_scores.append(score)
                    break

        
        if found_scores:
            print("Kết quả tra cứu điểm:")
            for score in found_scores:
                total_score = (score.midterm_score + score.final_score) / 2
                print(f"Học viên: {score.student_id}, Môn học: {score.course_id}, Điểm quá trình: {score.midterm_score}, Điểm kết thúc: {score.final_score}, Điểm tổng kết: {total_score}")
        else:
            print("Không tìm thấy điểm thi cho học viên tương ứng.")

    def hienThi(self):
        print("Danh sách điểm thi:")
        for score in self.scores:
            total_score = (score.midterm_score + score.final_score*2) / 3
            print(f"Học viên: {score.student_id}, Môn học: {score.course_id}, Điểm quá trình: {score.midterm_score}, Điểm kết thúc: {score.final_score}, Điểm tổng kết: {total_score}")

    def thongKe(self):
        print("Thống kê điểm thi:")
        soluong = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0
        }
        for score in self.scores:
            total_score = (score.midterm_score + score.final_score*2) / 3
            if 90 <= total_score <= 100 :
                soluong["A"] += 1
            elif 70 <= total_score < 90 :
                soluong["B"] += 1
            elif 50 <= total_score < 70 :
                soluong["C"] += 1
            elif total_score < 50 :
                soluong["D"] += 1
        
        for key in soluong.keys():
            print(f"Số lượng học sịnh đạt {key} là : {soluong[key]}")

    def ketXuat(self):
        file_name = "data_all.csv"
        datas = []
        for score in self.scores:
            total_score = (score.midterm_score + score.final_score*2) / 3
            student = [student for student in self.students if student.id == score.student_id]
            cource = [cource for cource in self.courses if cource.id == score.course_id]
            if len(student) != 0 and len(cource) != 0: 
                student = student[0]
                cource = cource[0]
                data = f"{score.student_id},{student.name},{student.date_of_birth},{student.gender}"
                data += f"{student.address},{student.phone}, {student.email},{cource.name}"
                data += f"{score.midterm_score},{score.final_score},{total_score}\n"
            
            datas.append(data)
           
            
        with open(file_name, 'w') as file:
            for data in datas:
                file.write(data)
            
        print(f"Kết xuất thông tin tại file {file_name}")

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
            qldt.ketXuat()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__" :
    menu = Menu()
    while True:
        menu.menu()
        choice = input("Nhập lựa chọn của bạn (0-3): ")
        print()

        if choice == "0":
            print("Đã thoát chương trình.")
            break
        elif choice == "1":
            qlhv = QuanLyHocVien('hocvien.txt')
            xuly_1(qlhv)

        elif choice == "2":
            qlmh = QuanLyMonHoc('monhoc.txt')
            xuly_2(qlmh)

        elif choice == "3":
            qldt = QuanLyDiemThi('diemthi.txt','monhoc.txt', 'hocvien.txt')
            xuly_3(qldt)
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")