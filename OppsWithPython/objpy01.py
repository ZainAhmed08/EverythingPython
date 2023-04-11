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


print("number of employees : " + str(Employee.no_Of_Employes))

zain = Employee("zain", "ahmed", 100000)

print("number of employees : " + str(Employee.no_Of_Employes))

faru = Employee("farhaan", "uzair", 121000)

print("number of employees : " + str(Employee.no_Of_Employes))

print(zain.fname+"'s salary : "+str(zain.salary))
print(faru.fname+"'s salary : "+str(faru.salary))
print(zain, faru)

zain.incrementSalary()
faru.incrementSalary()

print(zain.fname+"'s salary after increment: "+str(zain.salary))
print(faru.fname+"'s salary after increment: "+str(faru.salary))

print(zain.fname + "'s instance variables : " + str(zain.__dict__))
print("Employee class variables : " + str(Employee.__dict__))

# suppose zain wants to increase his salary and so to update the class variable increment
# we can use the function which uses class variables to set new increment value

Employee.increaseIncrement(2)
zain.incrementSalary()

print(zain.fname+"'s salary has been incremented to : " + str(zain.salary))
