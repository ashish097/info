

students = []

	
def get_students():
       #because this is list and we are adding a dictonary type so we have to return dictnory like wise
    
	sudents_title = []
	for i in students:
		sudents_title = i["name"].title()+ " " + i["student_id"].title()
		return sudents_title
	    
def print_studens_title():
	student_title = get_students()
	print ( student_title )

def add_students( name, student_id = 332 ):
	student1 = {"name": name, "student_id": student_id}
	students.append( student1 )


user = input("do u want to add user or not:")
student_name = input("enter the name:")
student_id = input("enter the idd:")



if user == "y":
    add_students( student_name, student_id )
    print("proced")
elif user == "n":
    print("canot be added")
else:
    print("Thnku")
    
print_studens_title()


