from StudentDemo.student import Student


class StudentManager():
    def __init__(self):
        self.student_list = []

    def run(self):
        # 加载学员
        self.laod_student()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入目标功能序号
            menu_num = int(input("please you need num"))
            # 工具用户输入的序号执行不同的序号功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_stuent()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出
                break

    # 显示功能菜单
    @staticmethod
    def show_menu():
        print("Please choice operation NO.:")
        print("[1]Add Student Message")
        print("[2]Delete Student Message")
        print("[3]Update Student Message")
        print("[4]Select Student Message")
        print("[5]Select Student All Message")
        print("[6]Save Student Message")
        print("[7]Exit")

    # 添加学员
    def add_student(self):
        name = input("Please Input Student Name:")
        gender = input("Please Input Student gender:")
        tel = input("Please Input Student tel:")
        # 创建学员对象
        student = Student(name, gender, tel)
        # 添加学员到学员列表
        self.student_list.append(student)
        print(self.student_list)

    # 删除学员
    def del_student(self):
        old_name = input("Please input you want delete student name: ")
        for i in self.student_list:
            if i.name == old_name:
                self.student_list.remove(i)
                break
        else:
            print("This student not found !")
        print(self.student_list)

    # 修改学员信息
    def modify_student(self):
        modify_name = input("Please input modify student name:")
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input("Student new name")
                i.gender = input("Student new gender")
                i.tel = input("Student new tel")
        else:
            print("This student not found!")


    # 查询学员的信息
    def search_student(self):
        search_name = input("Please input need search student name")
        for i in self.student_list:
            if search_name == i.name:
                print(f"name is {i.name},gender is {i.gender},tel is{i.tel}")
                break
        else:
            print("Not found")

    # x显示所有的学员信息
    def show_stuent(self):
        print('name\tgender\ttel')
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    # 保存学员信息
    def save_student(self):
        # 打开文件
        f = open('studenr.data','w')
        # 文件写入数据
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        # 关闭文件
        f.close()

    # 加载学员信息
    def laod_student(self):
        # 打开文件，尝试r打开，如果有异常w
        try:
            f = open('student.data','r')
        except :
            f = open("student.data","w")
        # 读取数据，文件读取出的数据是字符串还是还原列表类型[{}] 转化为[学员]
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        # 关闭文件
        f.close()
