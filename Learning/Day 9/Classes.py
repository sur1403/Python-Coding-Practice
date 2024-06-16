# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# School_bus = Vehicle(100, 10)
# print(School_bus.max_speed, School_bus.mileage)

# # OOP Exercise 2: Create a Vehicle class without any variables and methods
# class Vehicle:
#     def __init__(self):
#         pass

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass


# # Vehicle Name: School Volvo Speed: 180 Mileage: 12

# School_bus = Bus("volvo", 100, 20)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    

# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)


# school_bus = Bus("School Volvo", 180, 12)
# print(school_bus.seating_capacity())



# class Vehicle:
#     color = "White"
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# # Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12

# Bus_vehicle = Bus("School Volvo", 180, 12)
# Car_vehicle = Car("Audi Q5", 240, 18)

# print("Color: ", Bus_vehicle.color, "Vehicle name:" , Bus_vehicle.name, "Speed: ", Bus_vehicle.max_speed, "Mileage: ", Bus_vehicle.mileage)


# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will
# become the final amount = total fare + 10% of the total fare


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount = amount * 0.10
#         return amount

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus, Vehicle))
# print(type(School_bus))

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

Surbhi = Person("Sur", 20, "India")
print(Surbhi.name, Surbhi.age, Surbhi.country)

class Vehicle:
    def __init__(self) -> None:
        pass