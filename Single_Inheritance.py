#Parent Class
class Animal:
    def eat(self):
        print("This animal eat food")

class Dog(Animal):
    def bark(self):
        print("The dog bark")
dog=Dog()
print(dog.eat())
print(dog.bark())                