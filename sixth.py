#1class  in pyhton

class Student:
    pass

student = Student()
print(student)

new_student = Student()
print(new_student)


#2
students =[]
class Student:
    def add_student(self, name, student_id=332):
        student = {"name": name,"id":id}
        students.append(student)

student = Student()
student.add_student("mark")

print(student)
