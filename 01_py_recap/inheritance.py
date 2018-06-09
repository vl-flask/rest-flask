class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []
		
	def average(self):
		return sum(self.marks) / len(self.marks)

	@classmethod
	def friend(cls, original_student, friend_name):
		'''Return a new student in the same school as self.
		Will require salary for working students'''
		return cls(friend_name, original_student.school)
	
	# This is what we wd have to do for a Working student friend 
	@classmethod
	def fr2(cls, original_student, friend_name, salary):
		return cls(friend_name, original_student.school, salary)
#	def friend(self, friend_name):
#		'''Return a new student in the same school as self'''
#		return Student(friend_name, self.school)
		


class WorkingStudent(Student):
	def __init__(self, name, school, salary):
		super().__init__(name, school)
		self.salary = salary
class WorkingStudent2(Student):
	def __init__(self, name, school, salary, job):
		super().__init__(name, school)
		self.salary = salary
        self.job = job
        print("created")


		
		

	

anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary)
# friend = anna.friend("Greg")
friend = WorkingStudent.fr2(anna, "Greg", 17.50)
# friend = WorkingStudent.friend(anna, "Greg")
print(friend.name)
print(friend.school)

print(friend.salary) 
# an attribute error as Greg is a Student object

julia = WorkingStudent2(name="julia", school="cambridge", salary=15.0, job="shop assistant")
print("Julia")
print(julia.job_title, julia.salary)
julia.friend("Bill", 18.0, "security guard")
print("Bill is a student at {self.school}.")
print("He earns some extra money as {self.job_title}, and his wage is {self.salary}.")
