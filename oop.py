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


class Animal:
  def __init__(self, name, behaviour):
    self.name = name
    self.behaviour = behaviour

  def dog(self):
    return f"{self.name} is a breed of dog which {self.behaviour} at Premlata Devi Chaudhary."
  
dogesh = Animal("German Sephard", "barks")
print(dogesh.dog())

# inheritance

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def fullName(self):
    return f"{self.brand} is a brand of a car and {self.model} is a model."
  
class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

teslaCar = ElectricCar("Tesla", "model s", "85kWh")
print(teslaCar.model)


car1 = Car("Tata", "Nexon")
print(car1.fullName())


