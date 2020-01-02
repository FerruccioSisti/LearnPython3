#This exercise is working with inheritence

#Base class
class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

#Base class
class Person(object):
    def __init__(self, name):
        self.name = name
        #Person has some sort of pet
        self.pet = none

class Employee(Person):
    def __init__(self, name, salary):
        #Calls the constructor from the person class since Person is the super/parent class
        super(Employee, self).__init__(name)
        self.salary = salary

#Base class
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()
