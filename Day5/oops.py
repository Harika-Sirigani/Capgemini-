class Employee:
    def __init__(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name
        
        
    def details(self):
        return f"{self.emp_name} ID is {self.emp_id}"
    
    
emp1 = Employee(101,"Sita")
emp2 = Employee(102,"Ram")

print(emp1.details())
print(emp2.details())




