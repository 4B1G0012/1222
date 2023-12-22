class Course:
    def __init__(self, course_code, course_name, credit, compulsory, instructor, class_time):
        self.course_code = course_code
        self.course_name = course_name
        self.credit = credit
        self.compulsory = compulsory
        self.instructor = instructor
        self.class_time = class_time

    def display_info(self):
        print(f"課程代碼: {self.course_code}")
        print(f"課程名稱: {self.course_name}")
        print(f"學分數: {self.credit}")
        print(f"必選修: {'必修' if self.compulsory else '選修'}")
        print(f"任課老師: {self.instructor}")
        print(f"上課時間: {self.class_time}")

# 利用建構子建立物件
c1 = Course("C001", "套裝軟體應用", 3, True, "李宗儒", "星期五 8:00-11:00")
c2 = Course("C002", "體育生活", 3, True, "陳艷麗", "星期四 10:00-12:00")

# 顯示課程資訊
c1.display_info()
print("\n")
c2.display_info()
