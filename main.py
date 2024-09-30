# main.py dengan inputan statis
from classess.subclass import Car, ElectricCar
from classess.other_class import Bicycle

# Membuat objek dari class Car
car = Car("Toyota", "Corolla", 180, 1800, "Petrol", 4)
print(car.display_info())

# Membuat objek dari class ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 250, 100, 1.5)
print(electric_car.display_info())

# Membuat objek dari class Bicycle
bicycle = Bicycle("Polygon", "Mountain Bike", 21, "Aluminium")
print(bicycle.display_info())