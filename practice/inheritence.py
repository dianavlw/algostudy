#Inheritance = Allows a class to inherite attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass

class Cat(Animal):
    pass 

dog = Dog("Silver")
cat = Cat("Bloo")

print(dog.name)
print(cat.name)

dog.eat()
dog.sleep()