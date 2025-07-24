class employee:
    empolyee_number = 0
    @classmethod
    def employee_num(cls):
        print( cls.employee_number)




    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age = age 
        self.gender = gender
        self.salary = salary
        employee.empolyee_number +=1
    def totalsalary(self,target):
        totalsalary = self.salary + target 
        print(totalsalary)
    def print_all_attribute(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.salary)
emp1 = employee("Ahmed",25,"male",2500)
emp1.print_all_attribute()
emp1.totalsalary(1000)

emp2 = employee("bassant",21,"female",32000)
emp2.print_all_attribute()
emp2.totalsalary(1400)
#print( "employee number ",employee.empolyee_number)
employee.employee_num()