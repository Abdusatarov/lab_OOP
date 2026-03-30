class Student:
    def __init__(self, name: str, age: int):
        self.Name = name
        self.Age = age

    def displayinfo(self):
        print("Имя: ", self.Name, " Возраст: ", self.Age)

    def isadult(self) -> bool:
        return self.Age >= 18

    def greeting(self) -> str:
        return "Привет, меня зовут " + self.Name + ", мне " + str(self.Age) + " лет."


class Course:
    def __init__(self, name: str):
        self.Name = name
        self.Student1 = None
        self.Student2 = None
        self.Student3 = None
        self.students = []

    def displaycourse(self):
        print("Курс: ", self.Name)

    def student(self, student1: Student, student2: Student, student3: Student):
        self.Student1 = student1
        self.Student2 = student2
        self.Student3 = student3
        self.students = [s for s in (student1, student2, student3) if s is not None]

    def showstudents(self):
        if not self.students:
            print("На курсе нет студентов.")
            return
        idx = 1
        for s in self.students:
            print("Студент" + str(idx) + ": " + s.Name + ", Возраст: " + str(s.Age))
            idx += 1

    def constituents(self):
        return len(self.students)


class Professor:
    def __init__(self, name: str):
        self.Name = name


    def assigncourse(self, courses: Course):
        print(self.Name, "назначен преподавателем курса", courses.Name)


if __name__ == "__main__":
    s1 = Student("Айдар", 18)
    s2 = Student("Нурсултан", 17)
    s3 = Student("Алина", 19)

    s1.displayinfo()
    print(s2.greeting())
    print("Взрослый ли s3?", s3.isadult())

    course = Course("Математика")
    course.displaycourse()
    course.student(s1, s2, s3)
    course.showstudents()

    count = course.constituents()
    print("Количество студентов на курсе:", count)

    prof = Professor("Д.Смирнов")
    prof.assigncourse(course)
