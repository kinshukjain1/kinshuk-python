class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary 
        
    def display_emp(self):
        print("Employee ID:",self.emp_id)
        print("Salary:",self.salary)
        
class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department = department 
        
    def display(self):
        print("Department:",self.department)

    def display_all(self):
        self.display_person()
        self.display_emp()
        self.display()
         
manager1 = Manager("ABC",33,"1200",500000,"CS")

manager1.display_all()
