class Person:
    def __init__(self, name, age, program):
        self.__name = name
        self.__age = age
        self.program = program
    
    #public attribute program. Use @property to create getter methods
    @property
    def getName(self):
        return self.__name
    @property
    def getAge(self):
        return self.__age
    
    #define age setter for it to be accessed and modified
    def setAge(self, updatedAge):
        self.__age = updatedAge
        
def retrieveData(person):
    name = person.getName
    age = person.getAge
    program = person.program
    
    print(f"Name: {name}, Age: {age}, Program: {program}")

person = Person("Alnick", 20, "BSIT")

print("Initial Values:")
retrieveData(person)

person.__name = "Jerome" #this won't change the value of name because this is a private attribute
person.setAge(21) # this will change the value of age because I used the setAge method
person.program = "BSCS" # this will change the value of program because this is a public attribute


print("\nFinal Values:")
retrieveData(person)


# Output:
# +-----------------------------------------+
# |                                         |
# | Initial Values:                         |
# | Name: Alnick, Age: 20, Program: BSIT    |
# |                                         |
# | Final Values:                           |
# | Name: Alnick, Age: 21, Program: BSCS    |
# |                                         |
# +-----------------------------------------+


