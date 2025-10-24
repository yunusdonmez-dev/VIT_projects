class School():
    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
        
    def add_new_student(self, student_name, class_name): 
        self.students.append({"name": student_name, "class": class_name})

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        
    def view_student_list(self):
        for student in self.students:
            print(f"{student['name']} - Class: {student['class']}")
            
    def view_teacher_list(self):
        for teacher, branch in self.teachers.items():
            print(f"{teacher} - Branch: {branch}")  
            
my_school = School("Nilufer High School", 2014)
my_school.add_new_student("Helin", "10A")
my_school.add_new_student("Aya", "11B")
my_school.add_new_teacher("Ms. Hulya", "Math")
my_school.add_new_teacher("Ms. Yasemin", "Physics")

my_school.view_student_list()
my_school.view_teacher_list()
