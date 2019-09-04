class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print "totoal emp %d"%Employee.empCount
    def displayEmployees(self):
        print "Name:", self.name, ",Salary:", self.salary

ep1 = Employee("Tom",1000)
ep2 = Employee("Jhon",5000)
ep1.displayEmployees()
ep2.displayEmployees()
print "total emplyees", Employee.empCount

print "__doc__", Employee.__doc__
print "__name__", Employee.__name__
print "__module__", Employee.__module__
print "__bases__", Employee.__bases__
print "__dict__", Employee.__dict__
