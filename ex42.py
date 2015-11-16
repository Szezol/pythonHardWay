__author__ = 'Zoltan'

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## dog is an animal and has a name
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## cat is an animal and has a name
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has-a pet
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## emolyee is a person who has salary
        super(Employee, self).__init__(name)
        ##
        self.salary = salary

## fish is a class
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## 'satan' is cat
satan = Cat("Satan")

## 'Mary' is a person
mary = Person("Mary")

## 'Mary' has 'satan'
mary.pet = satan

## 'Frank' salary is 120000
frank = Employee("Frank", 120000)

## 'Frank' has a rover
frank.pet = rover

## 'flipper' is a fish
flipper = Fish()

## 'crouse' is a salmon
crouse = Salmon()

## 'harry' is a halibut
harry = Halibut()