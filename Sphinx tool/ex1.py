class Employee:
    """
    A class representing an employee.
 
    Attributes:
        name (str): The name of the employee.
        age (int): The age of the employee.
        department (str): The department the employee works in.
        salary (float): The salary of the employee.
    """
    def __init__(self, name, age, department, salary):
        """
        Initializes an Employee object.
 
        Parameters:
            name (str): The name of the employee.
            age (int): The age of the employee.
            department (str): The department the employee works in.
            salary (float): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
    def promote(self, raise_amount):
        """
        Promotes the employee and increases their salary.
 
        Parameters:
            raise_amount (float): The raise amount to increase the salary.
 
        Returns:
            str: A message indicating the promotion and new salary.
        """
        self.salary += raise_amount
        return f"{self.name} has been promoted! New salary: ${self.salary:.2f}"
    def retire(self):
        """
        Marks the employee as retired.
 
        Returns:
            str: A message indicating the retirement status.
        """
        # Some implementation for retiring an employee
        return f"{self.name} has retired. Thank you for your service!"
 
