import sys 
# import array as arr

# For getting input from input.txt file 
sys.stdin = open('input.txt', 'r')  
  
# Printing the Output to output.txt file 
sys.stdout = open('output.txt', 'w') 
class Car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
    def fullname(self):
        return f"{self.brand} {self.name}"  
class ElectriCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla=ElectriCar("Tesla","Model S","85KWH")

print(my_tesla   )
# brand=input()
# name=input()
# my_car=Car(brand,name)
# my_car=Car("Toyota","Corolla")
# print(my_car)
# print(my_car.brand,my_car.name)
# print(my_car.fullname())
   