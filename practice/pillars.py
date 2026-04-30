#1. Encapsulation → hide data

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

#2. Abstraction → hide complexity

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

#3. Inheritance → reuse code

class Car(Vehicle):
    def go(self):
        print("Driving")


#4. Polymorphism → same method, different behavior

def move(vehicle):
    vehicle.go()

move(Car())  # works


