# Create a Car class with atributes like brand and model.then create an instance of this class.

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
    

# my_car = Car("Kia", "Seltos")
# print("The brand of my car is:",my_car.brand)
# print(my_car.model)


# Class method and self
# Add a mrthod to the car class that displays the full name of the car (brand and model )

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def fullName(self):
#     return f"{self.brand} is the brand and {self.model} is the model"

# car1 = Car("Hyundai", "Verna")
# print(car1.brand)
# print(car1.model)
# print(car1.fullName())


# class Animal:
#   def __init__(self, name, behaviour):
#     self.name = name
#     self.behaviour = behaviour

#   def dog(self):
#     return f"{self.name} is a breed of dog which {self.behaviour} at Premlata Devi Chaudhary."
  
# dogesh = Animal("German Sephard", "barks")
# print(dogesh.dog())

# inheritance

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
  
#   def fullName(self):
#     return f"{self.brand} is a brand of a car and {self.model} is a model."
  
# class ElectricCar(Car):
#   def __init__(self, brand, model, battery_size):
#     super().__init__(brand, model)
#     self.battery_size = battery_size

# teslaCar = ElectricCar("Tesla", "model s", "85kWh")
# print(teslaCar.model)


# car1 = Car("Tata", "Nexon")
# print(car1.fullName())


class Student:
  def __init__(self, fullName, Age):
    self.fullName = fullName
    self.Age = Age

  def output(self):
     return f"The name of Student is {self.fullName}, age is {self.Age}. He is from {self.Address} and obtainded marks is {self.marks}" 

class A(Student):
  def __init__(self, fullName, Address, Age,  marks):
    super().__init__(fullName, Age)
    self.Address = Address
    self.marks = marks
B = A("Aayush", "Kathmandu", "23yrs", "95%")
print(B.output())



# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand 
#     self.model = model

#   def display(self):
#     return f"{self.brand} is the brand and the model is {self.model} and the mileage is {self.mileage}"
  
#   def displayForElecticCar(self):
#     return f"{self.brand} is the brand and the model is {self.model} and the battery size is {self.battery_size}"

# class Car(Vehicle):
#   def __init__(self, brand, model, mileage):
#     super().__init__(brand, model)
#     self.mileage = mileage

# class ElectricCar(Vehicle):
#   def __init__(self, model, brand, mileage, battery_size):
#     super().__init__(model, brand)
#     self.mileage = mileage
#     self.battery_size = battery_size

# Thar = Car("Mahindra", "Thar", "10km/lr")
# print(Thar.display())

# Tesla = ElectricCar("Tesla", "ModelS", "400km/charge", "120kWh")
# print(Tesla.displayForElecticCar())



class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def move(self):
    return "move"

class Car(Vehicle):
  pass

class Plane(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model)
    self.year = year

  def move(self):
    return f"{self.brand} plane flew in {self.year}"
  
class Boat(Vehicle):
  def __init__(self, brand, model, size):
    super().__init__(brand, model)
    self.size = size

  def move(self):
    print("Sail!")

car1 = Car("Tata", "Nexon")
print(car1.move())

plane1 = Plane("Buddha", "Domestic", "2025")
print(plane1.move())

boat1 = Boat("Titanic", "1956", "large")
boat1.move()