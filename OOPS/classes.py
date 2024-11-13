class Car:
    totalCreated = 0
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model
        Car.totalCreated += 1  #IMP this also can be used to access class variable
        # self.totalCreated = self.totalCreated + 1 #BUG this is still not working why I don't know 

    @staticmethod
    def carDescription():
        return f"This is the best car that ever existed"
    def fuelType(self):
        return "Gasoline" #REVIEW:

    def fullName(self):
        print(f"{self.__brand} {self.model}")

    def getBrand(self):
        return self.__brand + " is the brand"

class ElectricCar(Car):
    def __init__(self,brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
    
    # def batterySize(self):
    #     pass

    def fuelType(self):
        return "Electric"

myTesla = ElectricCar("Tesla", "Model S", "75 kWh")
myCar = Car("Nissan", "GT-R")
myCar2 = Car("Nissan", "R34")
myCar3 = Car("Lambo", "Aventador")
# print(myCar.fullName())
# print(myTesla.getBrand())
# print(myTesla.__brand)

# print(myCar.fuelType())
# print(myTesla.fuelType())
print(myCar.totalCreated)
print(Car.totalCreated)


# print(myCar3.carDescription())
print(Car.carDescription())