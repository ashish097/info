#1 nested function
def get_stud():
    students = ["ashish", "james"]
    students1 = "hi"
    def get_emp():
        students_emp = []
        for i in students:
            students_emp.append(i.title())
        return students_emp
    sttud_get_names = get_emp()
    print(sttud_get_names)

get_stud()


#2 read and write file


students = []

def add_student(name, srudent_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)
    
def save_file(student):
    try:
        f=open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f=open("students.txt", "r")
        for i in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")
            

read_file()

student_name =input("enter the name")
student_id =input("enter the id")

add_student(student_name,student_id)
save_file(student_name)




