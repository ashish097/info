#3 yield operations
students =[]

def read_file():
    try:
        f=open("students.txt", "r")
        for i in read_students(f):
            students.append(i)
        f.close()
    except Exception:
        print("could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
