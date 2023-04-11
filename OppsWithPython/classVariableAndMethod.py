class Employee:
    # class var
    increment = 1.5
    no_Of_Employes = 0

    # constructor
    def __init__(self, fname, lname, salary):
        print("Employee added")
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_Of_Employes += 1

    # function to increment salary
    def incrementSalary(self):
        self.salary = int(self.salary * self.increment)

    # if you want to change class variables and not instance variables
    # lets made a function which takes calss variabels and updates them
    @classmethod
    def increaseIncrement(cls, factor):
        cls.increment = factor

    # this is how to use class method as a constructor
    # this is also known as an alternative constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


# initlizing an instance using a class method as constructor , allthough this is a rarely used implementation
zain = Employee.from_str("zain-ahmed-41000")

print(zain.fname)
print(zain.lname)
print(zain.salary)

faru = Employee("farhaan", "uzair", 44000)

print(faru.fname)
print(faru.lname)
print(faru.salary)

strng = "hello-how-are-you"

message1, message2, message3, message4 = strng.split("-")
print(message2)
print(message4)
