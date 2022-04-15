# import sys
# sys.path.append("C:\\Users\\jaime\\Desktop\\GitHub\\Python")
from Python.advance_digital_experts.code import Bike
from Python.advance_digital_experts.code import Owner


bike = Bike({"license": "00001AAA", "color": "rojo", "type": "carretera",
            "description": "sin descripción"})
owner = Owner(bike)
print(owner.bike_description())
# print(bike.full_description)

# from code import Individual

# bike = Individual()

print("funciona")

