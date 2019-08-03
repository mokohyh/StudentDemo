class StudentManager():
    def __init__(self):
        self.student_list = []

    def run(self):
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
    # 添加学员
    def add_student(self):
        pass

    # 删除学员
    def del_student(self):
        pass

    # 修改学员信息
    def modify_student(self):
        pass

    # 查询学员的信息
    def search_student(self):
        pass

    # x显示所有的学员信息
    def show_stuent(self):
        pass

    # 保存学员信息
    def save_student(self):
        pass

    # 加载学员信息
    def laod_student(self):
        pass
