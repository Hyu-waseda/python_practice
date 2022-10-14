class Person:
 def __init__(self,
 first_name="", last_name=""):
 self.first_name = first_name
 self.last_name = last_name
 def get_name(self):
 return self.first_name + " " + self.last_name
 def __str__(self):
 return self.first_name + "/" + self.last_name
 def __repr__(self):
 return self.first_name + "*" + self.last_name
 if __name__ == "__main__":
 person1 = Person("John", "Smith")
 print(person1)


 class PersonWithBirthYear(Person):
def __init__(self,
first_name="", last_name="",
birth_year=None):
super().__init__(first_name, last_name)
self.birth_year = birth_year
def __str__(self):
return "{}/{} (born in {})".format(
self.first_name, self.last_name,
self.birth_year
)
 person = PersonWithBirthYear("John", "Smith", 1980)
 print(person)