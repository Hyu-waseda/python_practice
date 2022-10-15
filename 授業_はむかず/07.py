class Person:

	def __init__(self, first_name="", last_name=""):
 		self.first_name = first_name
 		self.last_name = last_name
	
	def	get_name(self):
 		return self.first_name + " " + self.last_name
	
	def	__str__(self):
 		return self.first_name + "/" + self.last_name

	def	__repr__(self):
 		return self.first_name + "*" + self.last_name

class PersonWithEmail(Person):

	def __init__(self, first_name="", last_name="", email=""):
		super().__init__(first_name, last_name)
		self.email = email
	
p = PersonWithEmail("John", "Smith", "john@example.com")
print(p.email)