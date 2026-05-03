# Instance method = best for operations on instances of the class(objects)
#static methods = best for utility functions that do not need access to class data
#                A method that belongs to a class rather than any object from that class(instance)
#               generally used fro general utility functions

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1= Employee("Eugune", "Manager")
employee2= Employee("Squidward", "Cashier")
employee3= Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Rocket Scientist"))

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())