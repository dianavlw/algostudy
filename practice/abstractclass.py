#Abstact class: A class that cannot be instatiated on its own: Meant to be subclassesd.
#               they can contain abstract methods, which are declared but have no implemetation
#               Abstract classes benefit:
#               1. Prevents instantiation of the class itself
#               2. Requires children to use inherited abstract methods


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you can drive the car")
    
    def stop(self):
        print("you stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("you stopped the motorcycle")


car = Car()
car.go()
car.stop()

motorcycle= Motorcycle()
motorcycle.go()
motorcycle.stop()


# go() is required in all vehicles 

from abc import ABC, abstractmethod
#ex. 1
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        return "Driving"

class Bike(Vehicle):
    def go(self):
        return "Riding"


#ex.2

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print("Paid with card")

class PayPal(PaymentStrategy):
    def pay(self, amount):
        print("Paid with PayPal")