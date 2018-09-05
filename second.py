Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> students = []
>>> def get_students():
	sudents_title = []
	for i in students:
		sudents_title = i.title()
		return sudents.title

	
>>> def add_students( name ):
	students.append( name )

	
>>> add_students( "mark" )
>>> add_students( "ashish" )
>>> add_students( "susil" )
>>> add_students( "elon" )
>>> add_students( "zaron" )
>>> def print_studens:
	
SyntaxError: invalid syntax
>>> def print_studens_title():
	student_title = get_students()
	print ( student_title)

	
>>> def add_students( name, student_id = 332 ):
	student1 = {"name": name, "student_id": student_id}
	students.append( name )

	
>>> def add_students( name, student_id = 332 ):
	student1 = {"name": name, "student_id": student_id}
	students.append( student1 )

	
>>> add_students( "mark", 345 )
>>> 
>>> for i in students
SyntaxError: invalid syntax
>>> def get_students():
	sudents_title = []
	for i in students:
		sudents_title = i.title()
		return sudents.title

	
>>> students_list = get_students()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    students_list = get_students()
  File "<pyshell#30>", line 5, in get_students
    return sudents.title
NameError: name 'sudents' is not defined
>>> for i in students
SyntaxError: invalid syntax
>>> for i in students
SyntaxError: invalid syntax
>>> for i in students:
	print ( i )

	
mark
ashish
susil
elon
zaron
{'name': 'mark', 'student_id': 345}
>>> def var_args(name, *arg):
	print(name)
	print(arg)

	
>>> var_args("axxam", "asdf", "0asdf", None, True)
axxam
('asdf', '0asdf', None, True)
>>> #inside the function print fun may not have quotes
>>> def var_args(name, **arg):
	print(name)
	print(arg["descript"], arg["fedback"])

	
>>> var_args("sinha", description="loves python", feedback="good", plural="True")
sinha
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    var_args("sinha", description="loves python", feedback="good", plural="True")
  File "<pyshell#44>", line 3, in var_args
    print(arg["descript"], arg["fedback"])
KeyError: 'descript'
>>> var_args("sinha", descript="loves python", feedback="good", plural="True")
sinha
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    var_args("sinha", descript="loves python", feedback="good", plural="True")
  File "<pyshell#44>", line 3, in var_args
    print(arg["descript"], arg["fedback"])
KeyError: 'fedback'
>>> var_args("sinha", description="loves python", fedback="good", plural="True")
sinha
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    var_args("sinha", description="loves python", fedback="good", plural="True")
  File "<pyshell#44>", line 3, in var_args
    print(arg["descript"], arg["fedback"])
KeyError: 'descript'
>>> var_args("sinha", descript="loves python", fedback="good", plural="True")
sinha
loves python good
>>> 
